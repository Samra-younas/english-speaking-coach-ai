import anthropic
from config import ANTHROPIC_API_KEY, SYSTEM_PROMPT


def get_client():
    """Creates and returns the Anthropic client."""
    return anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def ask_claude(client, user_text, chat_history):
    """Sends user message to Claude and returns (reply, updated_chat_history)."""
    chat_history.append({"role": "user", "content": user_text})

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=chat_history
    )

    reply = response.content[0].text
    chat_history.append({"role": "assistant", "content": reply})

    return reply, chat_history