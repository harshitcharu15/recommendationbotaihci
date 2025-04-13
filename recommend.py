import os
from openai import AzureOpenAI

endpoint = "https://kohli-m8kd5zju-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-4"
deployment = "gpt-4"

subscription_key = "4w2gf4ReoMWlu9H27ODLWOGW34JuRjUhI2H8fYnuvXIw7MfIU7dXJQQJ99BCACHYHv6XJ3w3AAAAACOGMfh9"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

prompt = "I want to travel to a quiet nature spot in Europe, with great hiking."

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a travel assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
