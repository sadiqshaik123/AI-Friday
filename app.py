from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

import os
import httpx

client = httpx.Client(verify=False)

llm= ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    api_key="",
    http_client=client
)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    print("AI:", llm.invoke(user_input).content)
    
