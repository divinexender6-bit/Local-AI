import os
import tempfile

import sounddevice as sd
from scipy.io.wavfile import write
from openai import OpenAI

from config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


def listen():
    sample_rate = 16000
    seconds = 5

    print("\n🎙️ DX Legacy is listening...")

    recording = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    file_path = tempfile.mktemp(suffix=".wav")

    write(
        file_path,
        sample_rate,
        recording
    )

    print("🧠 DX Legacy is processing your voice...")

    try:
        with open(file_path, "rb") as audio:

            transcription = client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=audio
            )

        return transcription.text.strip()

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)