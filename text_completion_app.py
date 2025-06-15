# text_completion_app.py

import os
import openai
from dotenv import load_dotenv
from openai.error import RateLimitError, APIConnectionError

# 1) Load your API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("Missing OPENAI_API_KEY in .env")

# 2) Declare your defaults here
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS  = 150
DEFAULT_TOP_P       = 1.0

# 3) Function that sends the prompt to OpenAI’s API
def complete(prompt: str,
             temperature: float = DEFAULT_TEMPERATURE,
             max_tokens: int = DEFAULT_MAX_TOKENS,
             top_p: float = DEFAULT_TOP_P) -> str:
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )
        return resp.choices[0].message.content.strip()
    except RateLimitError:
        print("[API error] Rate limit exceeded. Please wait and try again.")
    except APIConnectionError:
        print("[API error] Network issue. Check your internet connection.")
    except Exception as e:
        print(f"[API error] {e}")
    return ""

# 4) Main interactive loop
def main():
    print("=== Text Completion App ===")
    print("Type 'quit' or leave empty to exit.\n")

    while True:
        prompt = input("Prompt: ").strip()
        if not prompt or prompt.lower() == "quit":
            print("Goodbye!")
            break

        # Input validation
        if len(prompt) > 500:
            print("Prompt too long (max 500 chars). Please shorten it.")
            continue

        # Call the API with fixed parameters
        result = complete(prompt)
        print("\n→", result, "\n")

if __name__ == "__main__":
    main()

