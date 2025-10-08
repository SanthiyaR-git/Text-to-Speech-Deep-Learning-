from flask import Flask, render_template, request, send_file
from TTS.api import TTS
import os
import soundfile as sf

# Initialize Flask
app = Flask(__name__)

# Folder for audio output
OUTPUT_FILE = "static/output.wav"
os.makedirs("static", exist_ok=True)

# Load pretrained TTS model (Deep Learning)
# This downloads a high-quality model (may take a minute the first time)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

@app.route("/")
def index():
    return render_template("index.html", audio_file=None)

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form["text"]
    if not text.strip():
        return render_template("index.html", audio_file=None, message="Please enter text!")

    # Generate speech
    tts.tts_to_file(text=text, file_path=OUTPUT_FILE)

    return render_template("index.html", audio_file=OUTPUT_FILE, message="✅ Speech generated successfully!")

@app.route("/download")
def download_audio():
    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
