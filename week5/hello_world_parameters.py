import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me what ASL is",
        }
    ],
    model="gpt-4o",
    temperature=1,
    stop="American"
)

print(response.choices[0].message.content)
