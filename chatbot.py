"""
Simple AI Chatbot

Step 1:
- Take input from user and display output.

Step 2:
- Domain Expert Chatbot
- Restricts questions outside the configured domain.
"""

import os
import httpx
from openai import OpenAI


class DomainExpertChatBot:
    def __init__(self, api_key: str, base_url: str, model: str):

        self.model = model
        self.domain = "Java Backend Development"

        # TCS GenAI Lab SSL workaround
        http_client = httpx.Client(
            verify=False,
            timeout=60.0
        )

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=http_client
        )

        self.messages = [
            {
                "role": "system",
                "content": f"""
You are an expert assistant in {self.domain}.

STRICT RULES:
1. Answer ONLY questions related to {self.domain}.
2. If the question is outside {self.domain}, reply exactly:

Sorry, I am a domain expert chatbot and can only answer questions related to {self.domain}.

3. Keep answers concise and accurate.
4. Do not answer general knowledge questions.
5. Do not answer politics, sports, movies, current affairs, or entertainment questions.
"""
            }
        ]

    def ask(self, user_message: str) -> str:

        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=0.3,
                max_tokens=500
            )

            answer = response.choices[0].message.content

            self.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            return answer

        except Exception as e:
            return f"Connection/API Error:\n{str(e)}"


def main():

    # Preferred: Environment Variable
    API_KEY = os.getenv("GENAI_API_KEY")

    # Fallback (for hackathon/demo only)
    if not API_KEY:
        API_KEY = input("Enter your GenAI API Key: ").strip()

    # IMPORTANT:
    # Try /v1 first. If it fails, remove /v1.
    BASE_URL = "https://genailab.tcs.in/v1"

    MODEL = "azure_ai/genailab-maas-DeepSeek-V3-0324"

    try:
        chatbot = DomainExpertChatBot(
            api_key=API_KEY,
            base_url=BASE_URL,
            model=MODEL
        )

        print("=" * 60)
        print("Java Backend Development Expert Chatbot")
        print("Type 'exit' or 'quit' to close")
        print("=" * 60)

        while True:

            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\nGoodbye!")
                break

            response = chatbot.ask(user_input)

            print("\nBot:", response)

    except Exception as e:
        print("\nStartup Error:")
        print(str(e))


if __name__ == "__main__":
    main()