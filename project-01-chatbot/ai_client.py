import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file if running locally
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o")

client = OpenAI(api_key=API_KEY)

def generate_ai_response(message, history):
    """
    Convert Gradio chat history into OpenAI message format.
    """

    messages = []

    # Gradio history is a list of dicts: {"role": "...", "content": "..."}
    if history:
        for item in history:
            if isinstance(item, dict) and "role" in item and "content" in item:
                messages.append({
                    "role": item["role"],
                    "content": item["content"]
                })

    # Add the new user message
    messages.append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    return completion.choices[0].message.content

