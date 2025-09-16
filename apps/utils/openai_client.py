# utils/openai_client.py
from apps.utils.helpers import success
from ..system_setting.models import OpenAIApiCredentials
import openai

def get_openai_client():
    open_ai_api_credentials = OpenAIApiCredentials.objects.filter(is_active=True).first()
    if not open_ai_api_credentials:
        return False, False

    openai.api_key = open_ai_api_credentials.api_key
    return openai, open_ai_api_credentials.gpt_model
