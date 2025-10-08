# 🎙️ Deep Learning Text-to-Speech (TTS) Web App

A full-stack **Text-to-Speech (TTS)** web application built using **Flask** and **Deep Learning** (via [Coqui TTS](https://github.com/coqui-ai/TTS)).  
Users can enter any text, convert it into realistic speech, listen online, and download the generated audio.

---

## 🧠 Project Overview

Text-to-Speech (TTS) systems convert written text into spoken voice using deep learning models.  
This project provides an **interactive web app** where users can input text and instantly hear AI-generated speech.

**Key Features:**
- 🧬 Built on Deep Learning (Coqui TTS)
- 🎧 Converts any text into lifelike speech
- 💾 Saves generated audio (`output.wav`)
- 🌐 Clean frontend built with HTML + CSS
- ⚙️ Backend powered by Flask
- 📂 Single-file deployable architecture

---

## 📁 Project Structure

text-to-speech-app/
│
├── app.py # Flask backend + TTS generation logic
├── templates/
│ └── index.html # Frontend UI for text input and playback
├── static/
│ └── output.wav # Auto-generated speech output
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🧩 Tech Stack

| Component  | Technology Used |
|-------------|----------------|
| **Frontend** | HTML, CSS |
| **Backend** | Flask (Python) |
| **Model** | Coqui TTS (`tts_models/en/ljspeech/tacotron2-DDC`) |
| **Database (optional)** | SQLite (can be extended) |
| **Output Format** | WAV Audio |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/text-to-speech-app.git
cd text-to-speech-app


Install dependencies

Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate    # On Windows

Install all required packages:

pip install -r requirements.txt

requirements.txt

flask
TTS
soundfile

Run the Flask app
python app.py

Then open your browser and go to:

http://127.0.0.1:5000/

How It Works

The user enters any text in the web form.

Flask backend receives the text and sends it to the TTS model.

The Deep Learning model (Tacotron2-DDC) generates speech audio.

The output is saved as static/output.wav.

The webpage displays a player to listen or download the generated voice.

User Interface Preview

Input Form:

+---------------------------------------+
| Enter text to convert into speech...  |
| [ Generate Speech ]                   |
+---------------------------------------+


Output Section:

✅ Speech generated successfully!
▶️ [Play Audio]  📥 [Download]

Example Output
Input Text	Output Description
“Hello! Welcome to AI Voice Generator.”	Female American voice
“Artificial Intelligence is shaping the future.”	Smooth, natural-sounding speech

The generated file is saved automatically as:

static/output.wav

Future Improvements

🎙️ Add multi-language support

🧑‍🎤 Integrate voice cloning (e.g., YourTTS model)

🌍 Host app on Render / Heroku / AWS

🗃️ Add database logging for text history

🎛️ Add multiple voice styles & gender selection

📱 Improve UI/UX for mobile responsiveness

