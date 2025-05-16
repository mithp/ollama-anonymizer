import ollama
import re

# Initialize the Ollama client
client = ollama.Client()

def read_text_from_file(file_path):
    """Read text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_to_file(file_path, text):
    """Write text to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def anonymize_text_with_ner(client, model, text, prompt):
    """Anonymize text using NER model."""
    response = client.generate(model=model, prompt=prompt)
    return response

def process_text_in_chunks(client, model, text):
    """Process text in chunks and anonymize it."""
    chunks = text.split('\n')
    anonymized_text = ""

    for chunk in chunks:
        if chunk.strip():
            check_prompt = f"Is there any patient sensitive information in the following text? Return YES or NO: {chunk}"
            check_response = anonymize_text_with_ner(client, model, chunk, check_prompt)
            check_result = check_response.get('response', '').strip().split()

            if "YES" in check_result:
                anonymize_prompt = f"Anonymize the following text for sensitive information and replace with ** **. Return the text enclosed in <start> and <end> markers: {chunk}"
                anonymize_response = anonymize_text_with_ner(client, model, chunk, anonymize_prompt)
                anonymized_chunk = anonymize_response.get('response', '')
            else:
                anonymized_chunk = chunk
            anonymized_chunk = f"<start>{anonymized_chunk}<end>"
        else:
            anonymized_chunk = "<start> <end>"

        anonymized_text += anonymized_chunk + '\n'

    anonymized_text = re.findall(r'<start>(.*?)<\/?end>', anonymized_text, re.DOTALL)
    anonymized_text = '\n'.join(anonymized_text)
    cleaned_text = re.sub(r'<[^>]+>', '', anonymized_text)

    return cleaned_text
# Define the path to the input and output text files
base_path = "//your/PATH/"
input_file_path = base_path + "io_folder/data_for_input.txt"
output_file_path = base_path + "io_folder/data_for_output.txt"

# Read the text from the file
text = read_text_from_file(input_file_path)

# Process the text in chunks and anonymize it
anonymized_text = process_text_in_chunks(client, "phi4", text)

# Write the anonymized text to the output file
write_text_to_file(output_file_path, anonymized_text)

# Print a confirmation message
print("Anonymized text has been written to the output file.")