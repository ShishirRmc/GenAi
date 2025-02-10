import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions", #using openrouter to access claude sonnet api
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
  },
  data=json.dumps({
    "model": "anthropic/claude-3.5-haiku-20241022:beta",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ],
    
  })
)

print(response.json())