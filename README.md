# 🛡️ Text Anonymization with Ollama

This project demonstrates how to anonymize sensitive information from text using Ollama and large language models. Unlike traditional NLP pipelines, this approach dynamically adapts to various languages and formats, making it highly versatile for real-world applications.
---

## 🔗 Ollama Setup

1. Visit the Ollama website to install the Ollama CLI and set up your environment.
2. Download the required model (e.g., `phi4`) using the command:

   ```bash
   ollama run phi4
   ```

3. Ensure the Ollama server is running locally before executing the script.

---

## 📁 Project Structure

```
.
├── anonymizer.py              # Main script for anonymization
├── io_folder/
│   ├── data_for_input.txt     # Input file with raw text
│   └── data_for_output.txt    # Output file with anonymized text
```

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/mithp/ollama-anonymizer.git
   cd ollama-anonymizer
   ```

2. Place your input text in `io_folder/data_for_input.txt`.

3. Run the script:

   ```bash
   python anonymizer.py
   ```

4. The anonymized output will be saved in `io_folder/data_for_output.txt`.

---

## 🧪 Mock Example

**Input:**

```
John Doe, 32-vuotias ohjelmistosuunnittelija, kävi klinikalla 10.5.2025. Hän kertoi voivansa huonosti ja oireilevansa kuumeen, yskän ja hengenahdistuksen vuoksi. Lääkäri määräsi antibiootteja ja kehotti lepäämään viikon ajan. Johnilla on astma, joka saattaa pahentaa hänen oireitaan. Hänen potilastunnuksensa on JD123456 ja HETU 010190-1234.

Jane Smith, 45-vuotias potilas, jolla on suvussa sydän- ja verisuonitauteja, diagnosoitiin verenpainetauti ja hyperlipidemia. Hän käyttää tällä hetkellä ACE-estäjiä ja statiineja. Jane noudattaa tiukkaa ruokavaliota ja liikkuu säännöllisesti hallitakseen tilaansa. Hänen potilastunnuksensa on JS654321 ja HETU 020280-5678.

Kuopion sää on ollut tällä viikolla melko miellyttävä, lämpötilojen vaihdellessa 15°C ja 20°C välillä. Kaupunki koki ajoittaisia sadekuuroja, jotka auttoivat ylläpitämään puistojen vehreyttä.

Michael Johnson, 60-vuotias, kävi sairaalassa rutiinitarkastuksessa. Hänen verenpaineensa ja kolesterolitasonsa olivat normaalialueella, mutta hänelle suositeltiin verensokerin seurantaa rajalla olevan diabeteksen diagnoosin vuoksi. Michaelille on suositeltu vähentämään sokerin saantia ja lisäämään liikuntaa. Hänen potilastunnuksensa on MJ789012 ja HETU 030360-7890.

Paikallinen kirjasto järjestää ensi viikonloppuna kirjamessut, joissa esiintyy erilaisia kirjailijoita ja genrejä. Tapahtuma sisältää kirjan signeerauksia, lukutilaisuuksia ja työpajoja aloitteleville kirjoittajille. Messujen odotetaan houkuttelevan suuren yleisön yhteisöstä.

Emily Davis, 30-vuotias potilas, jolla on tyypin 1 diabetes, kävi seurantakäynnillä. Hän on hallinnut tilaansa hyvin säännöllisillä insuliinipistoksilla, liikunnalla ja tasapainoisella ruokavaliolla. Emily osallistuu myös diabeteksen tukiryhmään jakaakseen kokemuksia ja vinkkejä muiden kanssa. Hänen potilastunnuksensa on ED345678 ja HETU 040495-3456.

Kuopion vuosittainen maraton houkutteli tänä vuonna yli 1 000 osallistujaa, mikä teki siitä suuren menestyksen. Tapahtuma sisälsi erilaisia kategorioita, kuten täysmaraton, puolimaraton ja 10 km juoksu. Osallistujat vaihtelivat ammattiurheilijoista amatöörijuoksijoihin.

Robert Brown, 50-vuotias, otettiin sairaalaan pienen leikkauksen vuoksi, jossa poistettiin hyvänlaatuinen kasvain. Hänen odotetaan toipuvan täysin muutaman viikon kuluessa. Robertilla on tupakointihistoria, joka saattaa olla vaikuttanut kasvaimen kehittymiseen. Hänelle on suositeltu lopettamaan tupakointi ja noudattamaan terveellisempää elämäntapaa. Hänen potilastunnuksensa on RB901234 ja HETU 050575-9012.
```

**Output:**

```
****, **-vuotias ohjelmistosuunnittelija, kävi klinikalla **.**.2025. Hän kertoi voivansa huonosti ja oireilevansa kuumeen, yskän ja hengenahdistuksen vuoksi. Lääkäri määräsi antibiootteja ja kehotti lepäämään viikon ajan. **lla on astma, joka saattaa pahentaa hänen oireitaan. Hänen potilastunnuksensa on *** ja HETU **-****.
  
** **, 45-vuotias potilas, jolla on suvussa sydän- ja verisuonitauteja, diagnosoitiin verenpainetauti ja hyperlipidemia. Hän käyttää tällä hetkellä ACE-estäjiä ja statiineja. ** ** noudattaa tiukkaa ruokavaliota ja liikkuu säännöllisesti hallitakseen tilaansa. Hänen potilastunnuksensa on ** *** ja HETU ** **-****8.  
 
Kuopion sää on ollut tällä viikolla melko miellyttävä, lämpötilojen vaihdellessa 15°C ja 20°C välillä. Kaupunki koki ajoittaisia sadekuuroja, jotka auttoivat ylläpitämään puistojen vehreyttä. 
  
** **, 60-vuotias, kävi sairaalassa rutiinitarkastuksessa. Hänen verenpaineensa ja kolesterolitasonsa olivat normaalialueella, mutta hänelle suositeltiin verensokerin seurantaa rajalla olevan diabeteksen diagnoosin vuoksi. ** ** on suositeltu vähentämään sokerin saantia ja lisäämään liikuntaa. Hänen potilastunnuksensa on ** ** ja HETU **-**.  
 
Paikallinen kirjasto järjestää ensi viikonloppuna kirjamessut, joissa esiintyy erilaisia kirjailijoita ja genrejä. Tapahtuma sisältää kirjan signeerauksia, lukutilaisuuksia ja työpajoja aloitteleville kirjoittajille. Messujen odotetaan houkuttelevan suuren yleisön yhteisöstä. 
  
** **, **-vuotias potilas, jolla on tyypin 1 diabetes, kävi seurantakäynnillä. Hän on hallinnut tilaansa hyvin säännöllisillä insuliinipistoksilla, liikunnalla ja tasapainoisella ruokavaliolla. ** osallistuu myös diabeteksen tukiryhmään jakaakseen kokemuksia ja vinkkejä muiden kanssa. Hänen potilastunnuksensa on ** ja HETU **.  
 
Kuopion vuosittainen maraton houkutteli tänä vuonna yli 1 000 osallistujaa, mikä teki siitä suuren menestyksen. Tapahtuma sisälsi erilaisia kategorioita, kuten täysmaraton, puolimaraton ja 10 km juoksu. Osallistujat vaihtelivat ammattiurheilijoista amatöörijuoksijoihin. 
  
** **, -vuotias, otettiin sairaalaan pienen leikkauksen vuoksi, jossa poistettiin hyvänlaatuinen kasvain. Hänen odotetaan toipuvan täysin muutaman viikon kuluessa. Hänellä on tupakointihistoria, joka saattaa olla vaikuttanut kasvaimen kehittymiseen. Hänelle on suositeltu lopettamaan tupakointi ja noudattamaan terveellisempää elämäntapaa. Hänen potilastunnuksensa on ** ** ja HETU **-**.  
```

---

## ⚠️ Limitations

- A local Ollama setup is required with sufficient system resources.
- Output may vary depending on the model and prompt used.
- Prompt engineering is essential for consistent and accurate anonymization.

---

## 📌 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

- Ollama for providing the LLM interface.
