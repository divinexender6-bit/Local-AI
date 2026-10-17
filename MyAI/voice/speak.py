import subprocess


def speak(text):
    print(f"\n🔊 DX Legacy: {text}")

    subprocess.run(
        ["say", text],
        check=False
    )