import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def answer_question(question):
    message = [{'role': 'user', 'content': question}]

    response = client.chat.completions.create(
        model = "gpt-4o",
        stop = ['\n'],
        messages = message)
    answer = response.choices[0].message.content
    return answer
