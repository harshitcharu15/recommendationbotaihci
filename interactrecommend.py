import os
#from openai import OpenAI
from openai import AzureOpenAI

#client = OpenAI()
#from openai import AzureOpenAI


AZURE_API_KEY = "4w2gf4ReoMWlu9H27ODLWOGW34JuRjUhI2H8fYnuvXIw7MfIU7dXJQQJ99BCACHYHv6XJ3w3AAAAACOGMfh9"
AZURE_API_BASE = "https://kohli-m8kd5zju-eastus2.cognitiveservices.azure.com/"
#endpoint = "https://kohli-m8kd5zju-eastus2.cognitiveservices.azure.com/"
#model_name = "gpt-4"
#deployment = "gpt-4"

#subscription_key = "4w2gf4ReoMWlu9H27ODLWOGW34JuRjUhI2H8fYnuvXIw7MfIU7dXJQQJ99BCACHYHv6XJ3w3AAAAACOGMfh9"
AZURE_API_VERSION  = "2024-12-01-preview"
AZURE_DEPLOYMENT_NAME = "gpt-4"


client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_API_BASE,
)


#prompt = "I want to travel to a quiet nature spot in Europe, with great hiking."

def get_recommendation(user_input):
    response = client.chat.completions.create(model="gpt-4",  # Your deployment name
    messages=[
        {"role": "system", "content": "You are a helpful travel assistant who suggests travel destinations based on user preferences like weather, budget, and interests."},
        {"role": "user", "content": user_input}
    ])
    return response.choices[0].message.content

