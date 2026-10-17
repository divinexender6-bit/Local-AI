import threading
import tkinter as tk

from ai.brain import ask_ai
from ai.memory import load_memory

from voice.listen import listen
from voice.speak import speak

from avatar.character import Avatar


class DXLegacyApp:

    def __init__(self):

        self.avatar = Avatar()

        self.messages = load_memory()

        self.button = tk.Button(
            self.avatar.root,
            text="🎙️ TALK TO DX LEGACY",
            font=("Arial", 14),
            command=self.start_listening
        )

        self.button.pack(
            pady=10
        )

    def start_listening(self):

        self.button.config(
            state=tk.DISABLED
        )

        self.avatar.set_status(
            "🎙️ Listening..."
        )

        thread = threading.Thread(
            target=self.process_voice,
            daemon=True
        )

        thread.start()

    def process_voice(self):

        try:

            user_text = listen()

            if not user_text:

                self.update_status(
                    "I didn't hear anything."
                )

                return

            print(
                f"\n👤 You: {user_text}"
            )

            self.update_status(
                "🧠 Thinking..."
            )

            answer = ask_ai(
                self.messages,
                user_text
            )

            self.update_status(
                "🔊 Speaking..."
            )

            speak(answer)

            self.update_status(
                "DX Legacy is ready"
            )

        except Exception as error:

            print(
                "\n❌ ERROR:",
                error
            )

            self.update_status(
                "Something went wrong. Check Terminal."
            )

        finally:

            self.avatar.root.after(
                0,
                lambda: self.button.config(
                    state=tk.NORMAL
                )
            )

    def update_status(self, text):

        self.avatar.root.after(
            0,
            lambda: self.avatar.set_status(text)
        )

    def run(self):

        self.avatar.start()


if __name__ == "__main__":

    app = DXLegacyApp()

    app.run()