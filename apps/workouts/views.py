from apps.utils.openai_client import get_openai_client
from apps.workouts.models import Category, Macros,MealPlan, Meal, ProgressHistory, SuggestedWorkout, Swaps, Workout,Hydration, UserMealPlan
from rest_framework.views import APIView
from apps.workouts.serializers import WorkoutSerializer, CategorySerializer, MealPlanSerializer,ProgressHistorySerializer
from apps.utils.helpers import success, error
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile
import uuid
from io import BytesIO
from PIL import Image
import ast
import base64
import os



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
        
        suggested_workouts = SuggestedWorkout.objects.filter(user=user)

        filtered_workouts = []

        for suggested_workout in suggested_workouts:
            workouts = Workout.objects.filter(category=suggested_workout.workout.category, gender=gender)

            filtered_workouts.extend(workouts)

        serializer = WorkoutSerializer(filtered_workouts, many=True)

        return success(serializer.data, "Suggested workouts retrieved successfully.", 200)


class SuggestMealPlanAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        
        meal_plan = MealPlan.objects.filter(user=user).first()  

        if not meal_plan:
            return success(data=[], message="No meal plan found for this user.", code=200)
        
        # Serialize the meal plan data
        serializer = MealPlanSerializer(meal_plan)
        return success(serializer.data, message="Suggested meal plan retrieved successfully.")


class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
      
        categories = Category.objects.all()
        if(not categories):
            return error({"error": "No categories found for this user."}, 404)
        serializer = CategorySerializer(categories, many=True)
        return success(serializer.data, "Categories retrieved successfully.", 200)
    

class SearchWorkoutAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        q = request.query_params.get("q", None)
        user = request.user
        if not q:
            return error({"error": "No search query provided."}, 400)

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
            return error({"error": "No image uploaded"})

        mime_type = image.content_type

        if mime_type not in ["image/jpeg", "image/png", "image/jpg","image/heif"]:
            return error({"error": "Invalid image format. Please upload a JPEG or PNG image."}, 400)
        
        
        try:

            #if image not jpeg convert it to jpeg
            if mime_type != "image/jpeg":
                
                image_data = Image.open(request.FILES["image"])
                image_data = image_data.resize((1024, 1024))  

                output = BytesIO()
                image_data.convert("RGB").save(output, format="JPEG") 
                current_image_for_db = output.getvalue()
                image_base64 = base64.b64encode(current_image_for_db).decode("utf-8")
                
                # Create a ContentFile from the converted image for database storage
                converted_image = ContentFile(current_image_for_db)
                converted_image.name = f"{user.id}_{uuid.uuid4().hex}.jpg"
               
            else:
                image_data = image.read()
                image_base64 = base64.b64encode(image_data).decode("utf-8")
                # Reset file pointer for later use
                image.seek(0)
                converted_image = image



            # Retrieve all categories from the Category model and serialize them
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            json_data = serializer.data

            # Initialize OpenAI client
          
            openai, gpt_model = get_openai_client()
            
            response = openai.responses.create(
                model=gpt_model,
                input=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text", 
                            "text": f"""
                                        You are a human body fitness assistant. Below is a list of available workout categories: {json_data}. Based on the user's body image, suggest **relevant workout categories** and provide a **meal plan**. The meal plan should be tailored to the user's needs. 

                                        Please format your response as follows:

                                        ### SuggestedWorkoutCategories:
                                        Provide a list of relevant workout categories based on the user's body image. Each entry should be in the following format:
                                        - id (int)
                                        - name (string)

                                        Example:
                                        SuggestedWorkoutCategories = [
                                            {{'id': 6, 'name': 'Cardio Workout'}},
                                            {{'id': 4, 'name': 'Body Workout'}}
                                        ]

                                        ### MealPlan:
                                        Provide the **meal plan**. The meal plan should include:
                                        - goal (string): A description of the user's fitness goal (e.g., fat loss, muscle gain).
                                        - calories (string): The daily caloric intake (e.g., "2000 kcal/day").
                                        - hydration (string): Suggested daily hydration, e.g., "2-3 liters of water per day."
                                        - notes (string): Any additional notes or recommendations for the meal plan.
                                        - protein (string): Amount of protein (e.g., "150g of protein per day").

                                        Example:
                                        MealPlan = [
                                            "Fat loss with muscle retention; start with low-impact training 4–5x/week",
                                            "2300 kcal/day",
                                            "3.0-4.0 L/day",
                                            "High-protein, veggie-forward meals; keep sugary drinks/ultra-processed foods low",
                                            "180g"
                                        ]

                                        ### Macros:
                                        Provide the **macros** breakdown for the meal plan. This should include:
                                        - protein (string)
                                        - carbs (string)
                                        - fat (string)
                                        - fiber (string)

                                        Example:
                                        Macros = [
                                            "180g",  # protein
                                            "230g",  # carbs
                                            "73g",   # fat
                                            "35g"    # fiber
                                        ]

                                        ### Meal:
                                        Provide a list of **meals** for the user. Each meal should be described with:
                                        - meal name (string)
                                        - items (string): Description of the items in the meal.
                                        - approx_kcal (string): Approximate calories for the meal.
                                        - protein_g (string): Amount of protein in grams for the meal.

                                        Example:
                                        Meal = [
                                            ["Breakfast: Greek yogurt (350g, 2%) + oats (40g) + blueberries (1 cup) + almonds (10g)", "500 kcal", "40g"],
                                            ["Lunch: Grilled chicken breast (180g) + quinoa (1 cup cooked) + mixed salad, olive oil (1 tsp)", "600 kcal", "45g"]
                                        ]

                                        ### Swaps:
                                        Provide any **swaps** for the user's meals. This could include:
                                        - vegetarian (string): Vegetarian meal options.
                                        - easy_options (string): Simple, quick meal options that the user can consider.

                                        Example:
                                        Swaps = [
                                            "Vegetarian: tofu/tempeh stir-fry, lentil curry + brown rice, seitan fajitas",
                                            "Easy_options: rotisserie chicken or canned tuna/chickpeas, frozen veg, microwaveable brown rice"
                                        ]

                                        ### Hydration:
                                        Provide **hydration** guidelines, e.g., how much water the user should consume daily.

                                        Example:
                                        Hydration = [
                                            "Water 3.0–4.0 L/day; 1 glass before meals; 500 ml within 2h of training; add electrolytes if sweating heavily; limit sugary drinks/alcohol"
                                        ]

                                        ### UserMealPlan:
                                        Provide a **summary of the user's meal plan** (e.g., the number of meals, total calories, etc.).

                                        Example:
                                        UserMealPlan = [
                                            "4 meals + optional snack totaling ≈2300 kcal/day; ≈180g protein; macros as listed above"
                                        ]

                                        The workout categories should match one of the categories in the provided list.
                                        Evry points should include proper imojis
                                         """

                        },
                        {
                            "type": "input_image", 
                            "image_url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    ]
                }]
            )

            # Extract the result from the OpenAI response
            answer = response.output_text
            # Helper to safely parse sections
            def safe_parse(section_name, next_section):
                try:
                    return ast.literal_eval(answer.split(f"{section_name} = ")[1].split(f"\n{next_section} = ")[0].strip())
                except Exception:
                    return []

            suggested_workouts = safe_parse("SuggestedWorkoutCategories", "MealPlan")
            meal_plan = safe_parse("MealPlan", "Macros")
            macros = safe_parse("Macros", "Meal")
            meals = safe_parse("Meal", "Swaps")
            swaps = safe_parse("Swaps", "Hydration")
            hydration = safe_parse("Hydration", "UserMealPlan")
            user_meal_plan = safe_parse("UserMealPlan", "")

            # Save SuggestedWorkouts
            for workout in suggested_workouts:
                SuggestedWorkout.objects.update_or_create(user=user, workout_id=workout.get('id'))

            # Save MealPlan
            meal_plan_instance = MealPlan.objects.create(
                user=user,
                goal=meal_plan[0] if len(meal_plan) > 0 else "",
                calories=meal_plan[1] if len(meal_plan) > 1 else "",
                hydration=meal_plan[2] if len(meal_plan) > 2 else "",
                notes=meal_plan[3] if len(meal_plan) > 3 else ""
            )

            # Save Macros
            Macros.objects.create(
                meal_plan=meal_plan_instance,
                protein=macros[0] if len(macros) > 0 else "",
                carbs=macros[1] if len(macros) > 1 else "",
                fat=macros[2] if len(macros) > 2 else "",
                fiber=macros[3] if len(macros) > 3 else ""
            )

            # Save Meals
            for meal in meals:
                Meal.objects.create(
                    meal_plan=meal_plan_instance,
                    meal=meal[0] if len(meal) > 0 else "",
                    items=meal[1] if len(meal) > 1 else "",
                    approx_kcal=meal[2] if len(meal) > 2 else "",
                    protein_g=meal[3] if len(meal) > 3 else ""
                )

            # Save Swaps
            Swaps.objects.create(
                meal_plan=meal_plan_instance,
                vegetarian=swaps[0] if len(swaps) > 0 else "",
                easy_options=swaps[1] if len(swaps) > 1 else ""
            )

            # Save Hydration
            Hydration.objects.create(
                meal_plan=meal_plan_instance,
                hydration=hydration[0] if len(hydration) > 0 else ""
            )

            # Save UserMealPlan association
            UserMealPlan.objects.update_or_create(user=user, meal_plan=meal_plan_instance)

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


            # Prepare the content array
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

            # Only add previous image if it exists

            print(previous_image_base64)
            if previous_image_base64:
                content.append({
                    "type": "input_image", 
                    "image_url": f"data:image/jpeg;base64,{previous_image_base64}"
                })

            # Make the API call
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
                        # Append to current section if it's continuation text
                        sections[current_section] += ' ' + line
                
                return sections

        # Parse the response
            parsed_data = parse_response(response_text)

        # Create ProgressHistory entry
            ProgressHistory.objects.create(
                user=user,
                previous_image=previous_image_for_db,
                current_image=converted_image,  # Use the converted image here
                tips=parsed_data['tips'],
                differentiate_from_previous=parsed_data['differentiate_from_previous'],
                current_analysis=parsed_data['current_analysis'],
                status=parsed_data['status']
            )


            return success({
                "suggested_workouts": suggested_workouts,
                "meal_plan": meal_plan,
                "macros": macros,
                "meals": meals,
                "swaps": swaps,
                "hydration": hydration,
                "user_meal_plan": user_meal_plan,

            })

        except Exception as e:
            return error({"error": str(e)})

class ProgressHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        progress_history = ProgressHistory.objects.filter(user=user).order_by('-date')
        if(not progress_history):
            return success(data=[], message="No progress history found! Because you haven't uploaded any images.", code=200)
        serializer = ProgressHistorySerializer(progress_history, many=True)
        return success(serializer.data, "Progress history retrieved successfully.", 200)