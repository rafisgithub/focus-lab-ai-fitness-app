import os
from rest_framework.views import APIView
from apps.utils.helpers import success, error

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from openai import OpenAI

from apps.workouts.models import Category
from apps.workouts.serializers import CategorySerializer

GPT_MODEL = os.getenv('GPT_MODEL', 'gpt-5-nano-2025-08-07')

class OnboardingView(APIView):
    permission_classes = []
    
    def post(self, request, *args, **kwargs):

        body_image = request.data.get('body_image', '')
        onboarding_data = request.data.get('onboarding', {})
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        json_data = serializer.data

        gpt_input_data = {
            'onboarding': onboarding_data,
            'body_image': body_image,
            'categories': json_data
        }
        
        try:
            # Initialize OpenAI client
            client = OpenAI()
            
            response = client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a highly skilled fitness assistant trained to provide personalized workout plans, meal recommendations, and wellness advice. Analyze the user's onboarding data, body image, and available workout categories to create a tailored fitness journey. Ensure to select an appropriate workout category from the available options. Choose a workout form from the following categories: 
                        {categories}. Please make the recommendation motivational, practical, and include emojis to make it more engaging. Also, provide a healthy, balanced meal plan that complements the workout."""
                    },
                    {
                        "role": "user",
                        "content": json.dumps(gpt_input_data)
                    }
                ]
            )
            
            gpt_response = response.choices[0].message.content
            
            data = {
                'gpt_response': gpt_response
            }

            return success(data=data, message='Onboarding successful',)
        except Exception as e:
            return error(message='Onboarding failed')
