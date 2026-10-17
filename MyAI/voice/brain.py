from openai import OpenAI

from config import OPENAI_API_KEY, MODEL, SYSTEM_PROMPT
from ai.memory import add_message


if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY is missing. Check your .env file."
    )


client = OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(messages, user_text):
    add_message(messages, "user", user_text)

    conversation = [
        {
            "role": "developer",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(messages)

    response = client.responses.create(
        model=MODEL,
        input=conversation
    )

    answer = response.output_text.strip()

    add_message(messages, "assistant", answer)

    return answer