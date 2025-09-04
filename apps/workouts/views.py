import ast
import base64
import os
from openai import OpenAI
from apps.workouts.models import Category, Macros,MealPlan, Meal, ProgressHistory, SuggestedWorkout, Swaps, Workout,Hydration, UserMealPlan
from rest_framework.views import APIView
from apps.workouts.serializers import WorkoutSerializer, CategorySerializer, MealPlanSerializer
from apps.utils.helpers import success, error
from rest_framework.permissions import IsAuthenticated
import ast

GPT_MODEL = os.getenv('GPT_MODEL', 'gpt-5-nano-2025-08-07')

class WorkoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        gender = user.gender

        category_id = request.query_params.get("category_id", None)
        print(category_id)

        workouts = Workout.objects.filter(category=category_id, gender=gender) if category_id else Workout.objects.all()

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
        # Logic to suggest a meal plan for the user
        user = request.user
        
        # You can modify this logic to fetch a specific meal plan suggestion based on some criteria
        meal_plan = MealPlan.objects.filter(user=user).first()  # Fetches the user's first meal plan
        
        if not meal_plan:
            return error({"detail": "No meal plan found for this user."}, status=404)
        
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
        if not q:
            return error({"error": "No search query provided."}, 400)

        workouts = Workout.objects.filter(title__icontains=q)
        if not workouts:
            return error({"error": "No workouts found matching the search query."}, 404)

        serializer = WorkoutSerializer(workouts, many=True)
        return success(serializer.data, "Workouts retrieved successfully.", 200)

class UploadBodyImageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Retrieve the image from the request
        image = request.FILES.get("image")

        if not image:
            return error({"error": "No image uploaded"})

        try:
            # Convert the image to base64
            image_base64 = base64.b64encode(image.read()).decode("utf-8")

            # Retrieve all categories from the Category model and serialize them
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            json_data = serializer.data

            # Initialize OpenAI client
            client = OpenAI()

            # Make the OpenAI request
            response = client.responses.create(
                model=GPT_MODEL,
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
                                        Provide any **swaps** for the user’s meals. This could include:
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
                                        Provide a **summary of the user’s meal plan** (e.g., the number of meals, total calories, etc.).

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

            user = request.user

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
            

            ProgressHistory.objects.create(
                user=user,
                image=image,
                tips="",
            )

            return success({
                "suggested_workouts": suggested_workouts,
                "meal_plan": meal_plan,
                "macros": macros,
                "meals": meals,
                "swaps": swaps,
                "hydration": hydration,
                "user_meal_plan": user_meal_plan
            })

        except Exception as e:
            return error({"error": str(e)})