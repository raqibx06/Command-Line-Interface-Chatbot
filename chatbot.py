import os
import requests
import sys

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
MODEL = os.getenv("MODEL", "qwen2.5:3b")

def ask_ollama(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()
    return response.json()["response"]

def main():
    print("=" * 50)
    print(f" Ollama CLI Chatbot")
    print(f" Model: {MODEL}")
    print("  Type 'exit' or Ctrl+C to quit")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye!")
                sys.exit(0)

            print("Bot: thinking...\n")
            answer = ask_ollama(user_input)
            print(f"Bot: {answer}")

        except KeyboardInterrupt:
            print("\n Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\n Error: {e}")

if __name__ == "__main__":
    main()
