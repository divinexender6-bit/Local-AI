import tkinter as tk


class Avatar:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("DX Legacy AI")
        self.root.geometry("420x520")
        self.root.configure(bg="#111111")

        self.canvas = tk.Canvas(
            self.root,
            width=400,
            height=400,
            bg="#111111",
            highlightthickness=0
        )

        self.canvas.pack(pady=20)

        # Head
        self.canvas.create_oval(
            80,
            50,
            320,
            290,
            fill="#202020",
            outline="#4f8cff",
            width=4
        )

        # Left eye
        self.left_eye = self.canvas.create_oval(
            135,
            125,
            165,
            155,
            fill="#4f8cff"
        )

        # Right eye
        self.right_eye = self.canvas.create_oval(
            235,
            125,
            265,
            155,
            fill="#4f8cff"
        )

        # Mouth
        self.mouth = self.canvas.create_arc(
            145,
            175,
            255,
            240,
            start=200,
            extent=140,
            style=tk.ARC,
            outline="#4f8cff",
            width=4
        )

        self.status = tk.Label(
            self.root,
            text="DX Legacy is ready",
            bg="#111111",
            fg="white",
            font=("Arial", 16)
        )

        self.status.pack()

        self.blink()

    def blink(self):

        self.canvas.itemconfigure(
            self.left_eye,
            state=tk.HIDDEN
        )

        self.canvas.itemconfigure(
            self.right_eye,
            state=tk.HIDDEN
        )

        self.root.after(
            150,
            self.open_eyes
        )

    def open_eyes(self):

        self.canvas.itemconfigure(
            self.left_eye,
            state=tk.NORMAL
        )

        self.canvas.itemconfigure(
            self.right_eye,
            state=tk.NORMAL
        )

        self.root.after(
            3000,
            self.blink
        )

    def set_status(self, text):

        self.status.config(
            text=text
        )

    def start(self):

        self.root.mainloop()