from rest_framework.views import APIView
from apps.utils.helpers import success, error

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from openai import OpenAI

class OnboardingView(APIView):
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        # Get the data from the request
        body_image = request.data.get('body_image', '')
        onboarding_data = request.data.get('onboarding', {})
        
        # Combine the data for GPT input
        gpt_input_data = {
            'onboarding': onboarding_data,
            'body_image': body_image
        }
        
        try:
            # Initialize OpenAI client
            client = OpenAI()
            
            # Call GPT-3.5 API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a fitness assistant. Analyze the user's onboarding data and body image to provide personalized fitness recommendations and a beautiful meal plan"
                    },
                    {
                        "role": "user",
                        "content": json.dumps(gpt_input_data)
                    }
                ]
            )
            
            # Extract the GPT response
            gpt_response = response.choices[0].message.content
            
            # Prepare success response
            data = {
                # 'onboarding': onboarding_data,
                # 'body_image': body_image,
                'gpt_response': gpt_response
            }

            return success(data=data, message='Onboarding successful',)
        except Exception as e:
            return error(message='Onboarding failed')
