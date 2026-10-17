import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


def save_memory(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=2)


def add_message(messages, role, content):
    messages.append({
        "role": role,
        "content": content
    })

    # Keep the memory reasonably small.
    if len(messages) > 20:
        del messages[:-20]

    save_memory(messages)