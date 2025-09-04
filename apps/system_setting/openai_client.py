# utils/openai_client.py
from .models import OpenAIApiKey
import openai

def get_openai_client():
    active_key = OpenAIApiKey.objects.filter(is_active=True).first()
    if not active_key:
        raise ValueError("No active OpenAI API key found in the database.")
    
    openai.api_key = active_key.api_key
    return openai, active_key.gpt_model
