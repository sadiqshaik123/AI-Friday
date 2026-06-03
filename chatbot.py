"""
Simple AI Chatbot

This chatbot uses an OpenAI-compatible API endpoint.
"""

from openai import OpenAI


class BasicChatBot:
    """
    A simple chatbot class.
    """

    def __init__(self, api_key: str, base_url: str, model: str):
        # Save model name
        self.model = model

        # Create OpenAI client
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        # Store conversation history
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

    def ask(self, user_message: str) -> str:
        # Add user message
        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Call model
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=0.7
        )

        assistant_reply = response.choices[0].message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

        return assistant_reply


def main():
    API_KEY = "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"
    BASE_URL = "https://openrouter.ai/api/v1"
    MODEL = "openrouter/free"

    chatbot = BasicChatBot(API_KEY, BASE_URL, MODEL)

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        print("Bot:", chatbot.ask(user_input))


if __name__ == "__main__":
    main()
