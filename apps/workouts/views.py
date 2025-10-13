from apps.utils.openai_client import get_openai_client
from apps.workouts.models import Category, Macros,MealPlan, Meal, ProgressHistory, SuggestedWorkout, Swaps, Workout,Hydration, UserMealPlan, Day
from rest_framework.views import APIView
from apps.workouts.serializers import WorkoutSerializer, CategorySerializer, MealPlanSerializer,ProgressHistorySerializer,SuggestedWorkoutSerializer
from apps.utils.helpers import success, error
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile
import uuid
from io import BytesIO
from PIL import Image
import ast
import base64
import os
from django.db import models

from django.utils import timezone


class WorkoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        gender = user.gender

        category_id = request.query_params.get("category_id", None)
        print(category_id)

        workouts = Workout.objects.filter(gender=gender, category=category_id) if category_id else Workout.objects.filter(gender=gender)
        if(not workouts):
            return success(data=[], message="No workouts found for this user.", code=200)
        serializer = WorkoutSerializer(workouts, many=True)
        print(serializer.data)
        return success(serializer.data, "Workouts retrieved successfully.", 200)


class SuggestedWorkoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        gender = user.gender
        
        # Determine if user has progress history
        has_progress = ProgressHistory.objects.filter(user=user).exists()
        
        # Build query with gender filtering in both cases
        suggested_workouts = SuggestedWorkout.objects.filter(
            models.Q(workout__gender=gender) | models.Q(workout__gender='both')
        )
        
        # Add user filter based on progress history
        if has_progress:
            suggested_workouts = suggested_workouts.filter(user=user)
        else:
            suggested_workouts = suggested_workouts.filter(user__isnull=True)
        
        suggested_workouts = suggested_workouts.select_related('day', 'workout')
        
        # Organize and return response
        from collections import defaultdict
        day_wise_workouts = defaultdict(list)
        for suggestion in suggested_workouts:
            day_wise_workouts[suggestion.day.name].append(suggestion)
        
        response_data = {
            day: SuggestedWorkoutSerializer(workouts, many=True).data 
            for day, workouts in day_wise_workouts.items()
        }
        
        return success(response_data, "Suggested workouts retrieved successfully.", 200)



class SuggestMealPlanAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        query_date = request.query_params.get("date", None)
        date = timezone.datetime.fromisoformat(query_date) if query_date else None
        print(date)

        if(date):
            meal_plan = MealPlan.objects.filter(user=user, date__date=date).order_by('-id')

            if not meal_plan:
                return success(data=[], message=f"{query_date} you did not upload any images, so no meal plan available.", code=200)
        else:
            meal_plan = MealPlan.objects.filter(user=user).order_by('-id')

            if not meal_plan:
                return success(data=[], message="No meal plan has been created for you yet because you haven't uploaded any images.", code=200)
        
        # Serialize the meal plan data
        serializer = MealPlanSerializer(meal_plan,many=True)
        return success(serializer.data, message="Suggested meal plan retrieved successfully.")


class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
      
        categories = Category.objects.all()
        if(not categories):
            return success(data=[], message="No categories found.", code=200)
        serializer = CategorySerializer(categories, many=True)
        return success(serializer.data, "Categories retrieved successfully.", 200)
    

class SearchWorkoutAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        q = request.query_params.get("q", None)
        user = request.user
        if not q:
            return error(message="Search query parameter 'q' is required.", code=400)

        workouts = Workout.objects.filter(gender=user.gender, title__icontains=q)
        if not workouts:
            return success(data=[], message="No workouts found matching the search query.", code=200)

        serializer = WorkoutSerializer(workouts, many=True)
        return success(serializer.data, "Workouts retrieved successfully.", 200)


class UploadBodyImageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        image = request.FILES.get("image")
        current_image_for_db = None

        if not image:
            return error(message="No image provided.", code=400)

        mime_type = image.content_type

        if mime_type not in ["image/jpeg", "image/png", "image/jpg", "image/heif"]:
            return error(message="Invalid image format. Please upload a JPEG or PNG image.", code=400)
        
        try:
            # Image conversion logic
            if mime_type != "image/jpeg":
                image_data = Image.open(request.FILES["image"])
                image_data = image_data.resize((1024, 1024))  
                output = BytesIO()
                image_data.convert("RGB").save(output, format="JPEG") 
                current_image_for_db = output.getvalue()
                image_base64 = base64.b64encode(current_image_for_db).decode("utf-8")
                converted_image = ContentFile(current_image_for_db)
                converted_image.name = f"{user.id}_{uuid.uuid4().hex}.jpg"
            else:
                image_data = image.read()
                image_base64 = base64.b64encode(image_data).decode("utf-8")
                image.seek(0)
                converted_image = image

            # Get categories and days
            categories = Category.objects.all()
            days = Day.objects.all()
            
            # Initialize OpenAI client
            openai, gpt_model = get_openai_client()

            if not openai:
                return success(data=[], message="OpenAI client not configured.", code=200)
            
            # Prepare days data for the prompt
            days_data = [{"id": day.id, "name": day.name} for day in days]
            
            response = openai.responses.create(
                model=gpt_model,
                input=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text", 
                            "text": f"""
                                You are a professional fitness trainer. Based on the user's body image, create a comprehensive 7-day workout plan and complete meal plan.

                                Available Categories: {[{'id': cat.id, 'name': cat.name} for cat in categories]}
                                Available Days: {days_data}

                                Please generate a 7-day workout plan with the following structure:

                                For each day (Day 1 through Day 7), provide:
                                - A list of 3-8 workouts from the available categories
                                - Each workout should include: category ID, workout title, and ensure gender appropriateness
                                - Mix different muscle groups throughout the week
                                - Include cardio, strength training, and recovery days

                                Format your response as a JSON-like structure:

                                Day1 = [
                                    {{'category_id': 1, 'workout_title': 'Workout Title 1'}},
                                    {{'category_id': 2, 'workout_title': 'Workout Title 2'}},
                                    ...
                                ]

                                Day2 = [
                                    {{'category_id': 3, 'workout_title': 'Workout Title 3'}},
                                    {{'category_id': 4, 'workout_title': 'Workout Title 4'}},
                                    ...
                                ]

                                ... continue for all 7 days

                                Also provide complete meal plan information:

                                MealPlan = [
                                    "Fitness goal description",
                                    "Calorie recommendation",
                                    "Hydration guidance", 
                                    "Additional notes"
                                ]

                                Macros = [
                                    "Protein recommendation",
                                    "Carbs recommendation", 
                                    "Fat recommendation",
                                    "Fiber recommendation"
                                ]

                                Meal = [
                                    ["Breakfast: Meal description", "Food items", "Approx calories", "Protein in grams"],
                                    ["Lunch: Meal description", "Food items", "Approx calories", "Protein in grams"],
                                    ["Dinner: Meal description", "Food items", "Approx calories", "Protein in grams"],
                                    ["Snack: Meal description", "Food items", "Approx calories", "Protein in grams"]
                                ]

                                Swaps = [
                                    "Vegetarian swap options",
                                    "Easy preparation options"
                                ]

                                Hydration = [
                                    "Detailed hydration guidelines and recommendations"
                                ]

                                Ensure the workout plan is balanced and appropriate for the user's apparent fitness level.
                            """
                        },
                        {
                            "type": "input_image", 
                            "image_url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    ]
                }]
            )

            answer = response.output_text

            # Helper to parse sections
            def safe_parse(section_name, next_section=None):
                try:
                    if next_section:
                        content = answer.split(f"{section_name} = ")[1].split(f"\n{next_section} = ")[0].strip()
                    else:
                        content = answer.split(f"{section_name} = ")[1].strip()
                    return ast.literal_eval(content)
                except Exception as e:
                    print(f"Error parsing {section_name}: {e}")
                    return []

            # Parse workout days
            workout_plan = {}
            for i in range(1, 8):
                day_key = f"Day{i}"
                workout_plan[day_key] = safe_parse(day_key, f"Day{i+1}" if i < 7 else "MealPlan")

            # Parse meal plan data
            meal_plan_data = safe_parse("MealPlan", "Macros")
            macros_data = safe_parse("Macros", "Meal")
            meals_data = safe_parse("Meal", "Swaps")
            swaps_data = safe_parse("Swaps", "Hydration")
            hydration_data = safe_parse("Hydration")

            # Clear existing suggested workouts for this user
            SuggestedWorkout.objects.filter(user=user).delete()

            # Save 7-day workout plan to database
            saved_workouts_response = {}
            day_counter = 1
            
            for day_name, workouts in workout_plan.items():
                day_obj = Day.objects.get(id=day_counter)
                day_workouts = []
                
                for workout_data in workouts:
                    try:
                        # Find or create workout
                        workout, created = Workout.objects.get_or_create(
                            title=workout_data.get('workout_title', 'Custom Workout'),
                            category_id=workout_data.get('category_id'),
                            gender=user.gender if hasattr(user, 'gender') else 'male_and_female',
                            defaults={'video': 'workout_videos/default.mp4'}
                        )
                        
                        # Create suggested workout
                        suggested_workout = SuggestedWorkout.objects.create(
                            user=user,
                            day=day_obj,
                            workout=workout
                        )
                        
                        day_workouts.append({
                            "id": suggested_workout.id,
                            "workout": {
                                "id": workout.id,
                                "category": {
                                    "id": workout.category.id,
                                    "name": workout.category.name
                                },
                                "title": workout.title,
                                "gender": workout.gender,
                                "video": workout.video.url if workout.video else ""
                            }
                        })
                        
                    except Exception as e:
                        print(f"Error creating workout: {e}")
                        continue
                
                saved_workouts_response[day_name] = day_workouts
                day_counter += 1

            # Save meal plan
            meal_plan_instance = MealPlan.objects.create(
                user=user,
                goal=meal_plan_data[0] if len(meal_plan_data) > 0 else "",
                calories=meal_plan_data[1] if len(meal_plan_data) > 1 else "",
                hydration=meal_plan_data[2] if len(meal_plan_data) > 2 else "",
                notes=meal_plan_data[3] if len(meal_plan_data) > 3 else ""
            )

            # Save macros
            if macros_data:
                Macros.objects.create(
                    meal_plan=meal_plan_instance,
                    protein=macros_data[0] if len(macros_data) > 0 else "",
                    carbs=macros_data[1] if len(macros_data) > 1 else "",
                    fat=macros_data[2] if len(macros_data) > 2 else "",
                    fiber=macros_data[3] if len(macros_data) > 3 else ""
                )

            # Save meals
            if meals_data:
                for meal_data in meals_data:
                    Meal.objects.create(
                        meal_plan=meal_plan_instance,
                        meal=meal_data[0] if len(meal_data) > 0 else "",
                        items=meal_data[1] if len(meal_data) > 1 else "",
                        approx_kcal=meal_data[2] if len(meal_data) > 2 else "",
                        protein_g=meal_data[3] if len(meal_data) > 3 else ""
                    )

            # Save swaps
            if swaps_data:
                Swaps.objects.create(
                    meal_plan=meal_plan_instance,
                    vegetarian=swaps_data[0] if len(swaps_data) > 0 else "",
                    easy_options=swaps_data[1] if len(swaps_data) > 1 else ""
                )

            # Save hydration
            if hydration_data:
                Hydration.objects.create(
                    meal_plan=meal_plan_instance,
                    hydration=hydration_data[0] if len(hydration_data) > 0 else ""
                )

            # Save UserMealPlan association
            UserMealPlan.objects.update_or_create(
                user=user, 
                meal_plan=meal_plan_instance
            )

            # Handle progress history comparison
            current_image = image_base64
            previous_image_instance = ProgressHistory.objects.filter(user=user).order_by('-date').first()            

            previous_image_for_db = None
            if previous_image_instance and previous_image_instance.current_image:
                try:
                    with open(previous_image_instance.current_image.path, "rb") as f:
                        previous_image_data = f.read()
                    previous_image_base64 = base64.b64encode(previous_image_data).decode("utf-8")
                    previous_image_for_db = f"/media/{previous_image_instance.current_image.name}"
                except (FileNotFoundError, IOError):
                    previous_image_base64 = None
                    previous_image_for_db = None
            else:
                previous_image_base64 = None
                previous_image_for_db = None

            # Progress analysis
            content = [
                {
                    "type": "input_text", 
                    "text": f"""Compare the two uploaded images in terms of body composition, muscle tone, and overall fitness. 
                    1. Provide a detailed summary of the visible changes between the current and previous images.
                    2. Highlight any differences in muscle definition, fat reduction, posture, or other notable body transformations.
                    3. Offer actionable tips for improving body composition, including workout recommendations, dietary advice, or lifestyle changes.
                    4. Provide a general analysis of the user's current fitness level based on the comparison.
                    5. Conclude with a status update on the user's progress.
                    
                    Use the following format for the output:
                    - **Tips**: Actionable advice for improvement.
                    - **Differentiate from Previous**: A brief comparison summary between the two images.
                    - **Current Analysis**: General evaluation of the user's fitness progress.
                    - **Status**: Progress status."""
                },
                {
                    "type": "input_image", 
                    "image_url": f"data:image/jpeg;base64,{current_image}"
                }
            ]

            if previous_image_base64:
                content.append({
                    "type": "input_image", 
                    "image_url": f"data:image/jpeg;base64,{previous_image_base64}"
                })

            response = openai.responses.create(
                model=gpt_model,
                input=[{
                    "role": "user",
                    "content": content
                }]
            )

            response_text = response.output_text

            def parse_response(response_text):
                sections = {
                    'tips': '',
                    'differentiate_from_previous': '',
                    'current_analysis': '',
                    'status': ''
                }
                
                current_section = None
                lines = response_text.split('\n')
                
                for line in lines:
                    line = line.strip()
                    if line.startswith('- **Tips**:'):
                        current_section = 'tips'
                        sections['tips'] = line.replace('- **Tips**:', '').strip()
                    elif line.startswith('- **Differentiate from Previous**:'):
                        current_section = 'differentiate_from_previous'
                        sections['differentiate_from_previous'] = line.replace('- **Differentiate from Previous**:', '').strip()
                    elif line.startswith('- **Current Analysis**:'):
                        current_section = 'current_analysis'
                        sections['current_analysis'] = line.replace('- **Current Analysis**:', '').strip()
                    elif line.startswith('- **Status**:'):
                        current_section = 'status'
                        sections['status'] = line.replace('- **Status**:', '').strip()
                    elif current_section and line and not line.startswith('- **'):
                        sections[current_section] += ' ' + line
                
                return sections

            parsed_data = parse_response(response_text)

            # Create ProgressHistory entry
            ProgressHistory.objects.create(
                user=user,
                previous_image=previous_image_for_db,
                current_image=converted_image,
                tips=parsed_data['tips'],
                differentiate_from_previous=parsed_data['differentiate_from_previous'],
                current_analysis=parsed_data['current_analysis'],
                status=parsed_data['status']
            )

            return success({
                "suggested_workouts": saved_workouts_response,
                "meal_plan": meal_plan_data,
                "macros": macros_data,
                "meals": meals_data,
                "swaps": swaps_data,
                "hydration": hydration_data,
            })

        except Exception as e:
            return error(message="An error occurred while processing the image.", errors=str(e), code=500)

class ProgressHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        query_date = request.query_params.get("date", None)
        date = timezone.datetime.fromisoformat(query_date) if query_date else None


        if(date):

            progress_history = ProgressHistory.objects.filter(user=user, date__date=date).order_by('-id')
            if(not progress_history):
                return success(data=[], message=f"{query_date} you did not upload any images, so no progress history available.", code=200)
        else:
            progress_history = ProgressHistory.objects.filter(user=user).order_by('-id')

            if(not progress_history):
                return success(data=[], message="No progress history found! Because you haven't uploaded any images.", code=200)
            
        serializer = ProgressHistorySerializer(progress_history, many=True)
        return success(serializer.data, "Progress history retrieved successfully.", 200)