import subprocess


def open_calculator():

    subprocess.run(
        ["open", "-a", "Calculator"],
        check=False
    )


def open_notes():

    subprocess.run(
        ["open", "-a", "Notes"],
        check=False
    )