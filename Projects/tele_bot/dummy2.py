from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\rmcsh\\Documents\\GenAi\\LangGraph\\agents\\.env")

print("Environment variables loaded:", os.environ.keys())
google_api_key = os.getenv("GOOGLE_API_KEY")
telegram_api_key = os.getenv("TELEGRAM_API_KEY")

print("Google API Key:", google_api_key)
print("Telegram API Key:", telegram_api_key)