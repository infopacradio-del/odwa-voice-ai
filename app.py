from flask import Flask, request, send_file
from gtts import gTTS
import tempfile

app = Flask(__name__)

@app.route("/")
def home():
    return "Big Steppa Voice AI Backend is running ✅"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    text = data.get("text")

    if not text:
        return {"error": "No text provided"}

    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    return send_file(temp_file.name, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run()
