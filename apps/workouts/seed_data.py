from apps.workouts.models import Category, Day, Hydration, Macros, Meal, MealPlan, ProgressHistory, SuggestedWorkout, Swaps, Workout

def seed_categories():
    categories = [
        "3D Fitness Reels",
        "Arms Workout",
        "Back Workout",
        "Body Workout",
        "Calves Workout",
        "Cardio Workout",
        "Chest Workout",
        "Dumbbell Workout",
        "Forearms Workout",
        "Hamstrings Workout",
        "Hips Workout",
        "Jumping Workout",
        "Leg Workout",
        "Neck Workout",
        "Quadriceps Workout",
        "Random Workout",
        "Shoulders Workout",
        "Squat Workout",
        "Triceps Workout",
        "Waist Workout",
        "Male and Female"
    ]
    for category in categories:
        Category.objects.get_or_create(name=category)
    
    print("✅Categories seeded successfully.")

def seed_workouts():
        
    workouts = [
        {
            "title": "Fit & Fierce: 3D Female Workout Inspiration",
            "category": "3D Fitness Reels",
            "gender": "female",
            "video": "workout/Female/3D Fitness Reels Format/1.mp4",
        },
        {
            "title": "Strong & Toned: Female Arms Workout",
            "category": "Arms Workout",
            "gender": "female",
            "video": "workout/Female/Arms Workout/1.mp4",
        },
        {
            "title": "Back Power: Female Back Workout",
            "category": "Back Workout",
            "gender": "female",
            "video": "workout/Female/Back Workout/1.mp4",
        },
        {
            "title": "Full Body Blast: Female Body Workout",
            "category": "Body Workout",
            "gender": "female",
            "video": "workout/Female/Body Workout/1.mp4",
        },
        {
            "title": "Leg Sculpt: Female Calves Workout",
            "category": "Calves Workout",
            "gender": "female",
            "video": "workout/Female/Calves Workout/1.mp4",
        },
        {
            "title": "Cardio Burn: Female Cardio Workout",
            "category": "Cardio Workout",
            "gender": "female",
            "video": "workout/Female/Cardio Workout/1.mp4",
        },
        {
            "title": "Chest Strength: Female Chest Workout",
            "category": "Chest Workout",
            "gender": "female",
            "video": "workout/Female/Chest Workout/1.mp4",
        },
        {
            "title": "Dumbbell Power: Female Dumbbell Workout",
            "category": "Dumbbell Workout",
            "gender": "female",
            "video": "workout/Female/Dumbbell Workout/1.mp4",
        },
        {
            "title": "Forearm Focus: Female Forearms Workout",
            "category": "Forearms Workout",
            "gender": "female",
            "video": "workout/Female/Forearms Workout/1.mp4",
        },
        {
            "title": "Hamstring Power: Female Hamstrings Workout",
            "category": "Hamstrings Workout",
            "gender": "female",
            "video": "workout/Female/Hamstrings Workout/1.mp4",
        },
        {
            "title": "Hip Shaper: Female Hips Workout",
            "category": "Hips Workout",
            "gender": "female",
            "video": "workout/Female/Hips Workout/1.mp4",
        },
        {
            "title": "Jump & Burn: Female Jumping Workout",
            "category": "Jumping Workout",
            "gender": "female",
            "video": "workout/Female/Jumping Workout/1.mp4",
        },
        {
            "title": "Leg Day Power: Female Leg Workout",
            "category": "Leg Workout",
            "gender": "female",
            "video": "workout/Female/Leg Workout/1.mp4",
        },
        {
            "title": "Neck Mobility: Female Neck Workout",
            "category": "Neck Workout",
            "gender": "female",
            "video": "workout/Female/Neck Workout/1.mp4",
        },
        {
            "title": "Quad Strength: Female Quadriceps Workout",
            "category": "Quadriceps Workout",
            "gender": "female",
            "video": "workout/Female/Quadriceps Workout/1.mp4",
        },
        {
            "title": "Random Burn: Female Random Workout",
            "category": "Random Workout",
            "gender": "female",
            "video": "workout/Female/Random Workout/1.mp4",
        },
        {
            "title": "Shoulder Sculpt: Female Shoulders Workout",
            "category": "Shoulders Workout",
            "gender": "female",
            "video": "workout/Female/Shoulders Workout/1.mp4",
        },
        {
            "title": "Squat Power: Female Squat Workout",
            "category": "Squat Workout",
            "gender": "female",
            "video": "workout/Female/Squat Workout/1.mp4",
        },
        {
            "title": "Arm Definition: Female Triceps Workout",
            "category": "Triceps Workout",
            "gender": "female",
            "video": "workout/Female/Triceps Workout/1.mp4",
        },
        {
            "title": "Core Slimmer: Female Waist Workout",
            "category": "Waist Workout",
            "gender": "female",
            "video": "workout/Female/Waist Workout/1.mp4",
        },
        {
            "title": "Fit & Fierce: 3D Male Workout Inspiration",
            "category": "3D Fitness Reels",
            "gender": "male",
            "video": "workout/Male/3D Fitness Reels Format/1.mp4",
        },
        {
            "title": "Strong & Toned: Male Arms Workout",
            "category": "Arms Workout",
            "gender": "male",
            "video": "workout/Male/Arms Workout/1.mp4",
        },
        {
            "title": "Back Power: Male Back Workout",
            "category": "Back Workout",
            "gender": "male",
            "video": "workout/Male/Back Workout/1.mp4",
        },
        {
            "title": "Full Body Blast: Male Body Workout",
            "category": "Body Workout",
            "gender": "male",
            "video": "workout/Male/Body Workout/1.mp4",
        },
        {
            "title": "Leg Sculpt: Male Calves Workout",
            "category": "Calves Workout",
            "gender": "male",
            "video": "workout/Male/Calves Workout/1.mp4",
        },
        {
            "title": "Cardio Burn: Male Cardio Workout",
            "category": "Cardio Workout",
            "gender": "male",
            "video": "workout/Male/Cardio Workout/1.mp4",
        },
        {
            "title": "Chest Strength: Male Chest Workout",
            "category": "Chest Workout",
            "gender": "male",
            "video": "workout/Male/Chest Workout/1.mp4",
        },
        {
            "title": "Dumbbell Power: Male Dumbbell Workout",
            "category": "Dumbbell Workout",
            "gender": "male",
            "video": "workout/Male/Dumbbell Workout/1.mp4",
        },
        {
            "title": "Forearm Focus: Male Forearms Workout",
            "category": "Forearms Workout",
            "gender": "male",
            "video": "workout/Male/Forearms Workout/1.mp4",
        },
        {
            "title": "Hamstring Power: Male Hamstrings Workout",
            "category": "Hamstrings Workout",
            "gender": "male",
            "video": "workout/Male/Hamstrings Workout/1.mp4",
        },
        {
            "title": "Hip Shaper: Male Hips Workout",
            "category": "Hips Workout",
            "gender": "male",
            "video": "workout/Male/Hips Workout/1.mp4",
        },
        {
            "title": "Jump & Burn: Male Jumping Workout",
            "category": "Jumping Workout",
            "gender": "male",
            "video": "workout/Male/Jumping Workout/1.mp4",
        },
        {
            "title": "Leg Day Power: Male Leg Workout",
            "category": "Leg Workout",
            "gender": "male",
            "video": "workout/Male/Leg Workout/1.mp4",
        },
        {
            "title": "Neck Mobility: Male Neck Workout",
            "category": "Neck Workout",
            "gender": "male",
            "video": "workout/Male/Neck Workout/1.mp4",
        },
        {
            "title": "Quad Strength: Male Quadriceps Workout",
            "category": "Quadriceps Workout",
            "gender": "male",
            "video": "workout/Male/Quadriceps Workout/1.mp4",
        },
        {
            "title": "Random Burn: Male Random Workout",
            "category": "Random Workout",
            "gender": "male",
            "video": "workout/Male/Random Workout/1.mp4",
        },
        {
            "title": "Shoulder Sculpt: Male Shoulders Workout",
            "category": "Shoulders Workout",
            "gender": "male",
            "video": "workout/Male/Shoulders Workout/1.mp4",
        },
        {
            "title": "Squat Power: Male Squat Workout",
            "category": "Squat Workout",
            "gender": "male",
            "video": "workout/Male/Squat Workout/1.mp4",
        },
        {
            "title": "Arm Definition: Male Triceps Workout",
            "category": "Triceps Workout",
            "gender": "male",
            "video": "workout/Male/Triceps Workout/1.mp4",
        },
        {
            "title": "Core Slimmer: Male Waist Workout",
            "category": "Waist Workout",
            "gender": "male",
            "video": "workout/Male/Waist Workout/1.mp4",
        },
        {
            "title": "Male and Female Full Body Workout",
            "category": "Male and Female",
            "gender": "male_and_female",
            "video": "workout/male_and_female/Male and Female/1.mp4"
        },
        {
            "title": "Male and Female Full Body Workout",
            "category": "Male and Female",
            "gender": "male_and_female",
            "video": "workout/male_and_female/Male and Female/2.mp4"
        },
        {
            "title": "Male and Female Full Body Workout",
            "category": "Male and Female",
            "gender": "male_and_female",
            "video": "workout/male_and_female/Male and Female/3.mp4"
        },
        {
            "title": "Male and Female Full Body Workout",
            "category": "Male and Female",
            "gender": "male_and_female",
            "video": "workout/male_and_female/Male and Female/4.mp4"
        },
        {
            "title": "Male and Female Full Body Workout",
            "category": "Male and Female",
            "gender": "male_and_female",
            "video": "workout/male_and_female/Male and Female/5.mp4"
        }

    ]


    for workout in workouts:
        category = Category.objects.get(name=workout["category"])
        Workout.objects.get_or_create(
            title=workout["title"],
            category=category,
            gender=workout["gender"],
            video=workout["video"],
        )

    print("✅Workouts seeded successfully.")


def seed_day():
    days = [
        "Day 1",
        "Day 2",
        "Day 3",
        "Day 4",
        "Day 5",
        "Day 6",
        "Day 7"
    ]
    for day in days:
        Day.objects.get_or_create(name=day)
    print("✅ Days seeded successfully.")


def seed_suggested_workouts():

    seed_suggested_workouts = []

    # Simple round-robin distribution
    for workout_id in range(1, 41):
        day_id = ((workout_id - 1) % 7) + 1  # Distribute across days 1-7
        seed_suggested_workouts.append({
            "day_id": day_id,
            "workout_id": workout_id,
        })

    for swo in seed_suggested_workouts:
        SuggestedWorkout.objects.get_or_create(**swo)

    print("✅ Suggested Workouts seeded successfully.")


def seed_suggested_meal_plans():
    seed_suggested_meal_plans = [
        {
            "user_id": 1,   
            "goal": "Weight Loss 🏃‍♂️🔥",
            "calories": "1500 kcal 🍏, designed to help shed those extra pounds while still providing enough energy for your day.",
            "hydration": "2 liters 💧, essential to keep you feeling energized and hydrated as you work towards your goal.",
            "notes": "This plan focuses on high-protein 🥩 meals to support muscle preservation while cutting down on carbs 🥦, which are reduced to help burn fat. It’s important to stay away from sugary foods 🍩 that can slow down the weight loss process.",
        },
        {
            "user_id": 1,   
            "goal": "Muscle Gain 💪🏽🏋️‍♂️",
            "calories": "2500 kcal 🍗, formulated to give you the energy needed to build muscle while fueling intense workouts and recovery.",
            "hydration": "3 liters 💧, which is crucial to support muscle repair and keep you hydrated throughout the day, especially after a tough workout.",
            "notes": "This meal plan is rich in complex carbs 🍠 to fuel your body with sustained energy, along with healthy fats 🥑 to aid in muscle growth and hormone regulation. Make sure to focus on getting a balanced meal immediately after your workout 💥 to maximize recovery and muscle development.",
        },
        {
            "user_id": 1,   
            "goal": "Endurance Training 🏃‍♀️💨",
            "calories": "2200 kcal 🍞, designed to provide sustained energy for long-distance training, while keeping your body in top condition for endurance events.",
            "hydration": "3.5 liters 💧, vital for rehydrating during long runs or cycling sessions, keeping your body refreshed and energized.",
            "notes": "This plan includes a balance of carbs 🍚 and lean proteins 🥩 to fuel long workouts and aid muscle recovery. Stay hydrated and include natural electrolytes like coconut water 🥥 to replenish lost minerals.",
        },
        {
            "user_id": 1,   
            "goal": "Fat Loss & Toning 💃✨",
            "calories": "1800 kcal 🥗, focusing on reducing body fat while keeping muscle tone and definition intact.",
            "hydration": "2.5 liters 💧, to ensure your metabolism stays active and your skin looks glowing as you work towards a leaner body.",
            "notes": "This plan is designed with a balance of lean protein 🥩, vegetables 🥦, and healthy fats 🥑, while limiting simple sugars 🍭 and processed foods. A high-protein, low-carb approach helps reduce fat while maintaining muscle tone.",
        },
        {
            "user_id": 1,   
            "goal": "General Health & Wellness 🌱🌞",
            "calories": "2000 kcal 🥑, designed to provide a well-rounded, balanced diet with a focus on overall health and wellness.",
            "hydration": "2.5 liters 💧, crucial for keeping your organs functioning properly and helping you feel energized throughout the day.",
            "notes": "This plan focuses on whole foods 🥦, healthy fats 🥑, and clean proteins 🥩, with plenty of fruits 🍇 and vegetables 🥗 to boost your immune system. It also supports digestive health and promotes a healthy gut 🌱.",
        },
        {
            "user_id": 1,   
            "goal": "Keto Diet 🍳🥓",
            "calories": "2000 kcal 🧀, designed for those who are following a keto lifestyle, prioritizing fats and proteins while keeping carbs very low.",
            "hydration": "2 liters 💧, essential to help balance electrolytes and prevent dehydration while following a high-fat diet.",
            "notes": "This plan includes high-quality fats 🥑, such as avocado and olive oil, and moderate protein sources 🥩. It avoids starchy foods 🍞 and focuses on maintaining a state of ketosis, which helps burn fat efficiently. Remember to stay hydrated and incorporate electrolytes into your meals.",
        },
        {
            "user_id": 1,   
            "goal": "Vegan Lifestyle 🌱🥑",
            "calories": "2000 kcal 🥒, designed for those following a vegan diet, focusing on plant-based proteins and healthy fats.",
            "hydration": "2.5 liters 💧, crucial for keeping your body hydrated and supporting energy levels throughout the day.",
            "notes": "This plan emphasizes plant-based proteins 🥙, healthy fats 🥑, and fiber-rich fruits and vegetables 🍇. It excludes all animal products 🐄 and encourages whole, natural foods. Stay mindful of vitamin B12 🧴 and iron-rich plant foods 🥬.",
        },
        {
            "user_id": 1,   
            "goal": "Paleo Diet 🥩🍠",
            "calories": "2000 kcal 🥩, designed for those following a paleo diet, focusing on whole foods and eliminating processed items.",
            "hydration": "2.5 liters 💧, important for maintaining hydration levels while consuming a high-protein diet.",
            "notes": "This plan emphasizes lean meats 🥩, fish 🐟, fruits 🍏, and vegetables 🥦, while avoiding grains 🍞, legumes, and dairy 🥛. It's designed to promote weight loss and improve overall health."
        }
    ]
    for smp in seed_suggested_meal_plans:
        MealPlan.objects.get_or_create(**smp)
    print("✅ Suggested Meal Plans seeded successfully.")


def seed_macros():
    seed_macros = [
        {
            "meal_plan_id": 1,
            "protein": "150g",
            "carbs": "100g",
            "fat": "50g",
            "fiber": "30g"
        },
        {
            "meal_plan_id": 2,
            "protein": "200g",
            "carbs": "250g",
            "fat": "70g",
            "fiber": "25g"
        },
        {
            "meal_plan_id": 3,
            "protein": "180g",
            "carbs": "220g",
            "fat": "60g",
            "fiber": "28g"
        },
        {
            "meal_plan_id": 4,
            "protein": "160g",
            "carbs": "150g",
            "fat": "55g",
            "fiber": "32g"
        },
        {
            "meal_plan_id": 5,
            "protein": "170g",
            "carbs": "180g",
            "fat": "65g",
            "fiber": "30g"
        },
        {
            "meal_plan_id": 6,
            "protein": "140g",
            "carbs": "50g",
            "fat": "120g",
            "fiber": "20g"
        },
        {
            "meal_plan_id": 7,
            "protein": "130g",
            "carbs": "200g",
            "fat": "70g",
            "fiber": "35g"
        },
        {
            "meal_plan_id": 8,
            "protein": "150g",
            "carbs": "200g",
            "fat": "60g",
            "fiber": "30g"
        }
    ]
    for macro in seed_macros:
        Macros.objects.get_or_create(**macro)
    print("✅ Macros seeded successfully.")

def seed_meals():
    meals = [
        {
            "meal_plan_id": 1,
            "meal": "Breakfast",
            "items": "Oatmeal with berries and a scoop of protein powder",
            "approx_kcal": "350 kcal",
            "protein_g": "30g"
        },
        {
            "meal_plan_id": 2,
            "meal": "Lunch",
            "items": "Grilled chicken salad with mixed greens and vinaigrette",
            "approx_kcal": "450 kcal",
            "protein_g": "40g"
        },
        {
            "meal_plan_id": 3,
            "meal": "Dinner",
            "items": "Baked salmon with quinoa and steamed broccoli",
            "approx_kcal": "500 kcal",
            "protein_g": "50g"
        },
        {
            "meal_plan_id": 4,
            "meal": "Snack",
            "items": "Greek yogurt with almonds",
            "approx_kcal": "200 kcal",
            "protein_g": "20g"
        },
        {
            "meal_plan_id": 5,
            "meal": "Breakfast",
            "items": "Scrambled eggs with spinach and whole grain toast",
            "approx_kcal": "400 kcal",
            "protein_g": "35g"
        },
        {
            "meal_plan_id": 6,
            "meal": "Lunch",
            "items": "Turkey and avocado wrap with a side of carrot sticks",
            "approx_kcal": "450 kcal",
            "protein_g": "40g"
        },
        {
            "meal_plan_id": 7,
            "meal": "Dinner",
            "items": "Stir-fried tofu with mixed vegetables and brown rice",
            "approx_kcal": "500 kcal",
            "protein_g": "45g"
        },
        {
            "meal_plan_id": 8,
            "meal": "Snack",
            "items": "Cottage cheese with pineapple chunks",
            "approx_kcal": "200 kcal",
            "protein_g": "25g"
        }
    ]

    for meal in meals:
        Meal.objects.get_or_create(**meal)
    print("✅ Meals seeded successfully.")


def seed_swaps():
    seed_swaps = [
        {
            "meal_plan_id": 1,
            "vegetarian": "Replace chicken with tofu or tempeh. Use plant-based protein powder instead of whey.",
            "easy_options": "Pre-made oatmeal packets, canned beans, frozen berries for quick preparation."
        },
        {
            "meal_plan_id": 2,
            "vegetarian": "Substitute chicken with chickpeas or lentils. Use plant-based protein sources like seitan.",
            "easy_options": "Canned chickpeas, pre-cooked lentils, store-bought salad mixes for convenience."
        },
        {
            "meal_plan_id": 3,
            "vegetarian": "Replace salmon with firm tofu or plant-based fish alternatives. Use vegetable broth instead of fish-based ingredients.",
            "easy_options": "Frozen quinoa packets, pre-cut broccoli, canned beans for quick meals."
        },
        {
            "meal_plan_id": 4,
            "vegetarian": "Use plant-based yogurt alternatives. Replace dairy with almond or soy-based products.",
            "easy_options": "Single-serving yogurt cups, pre-portioned nuts, ready-to-eat snacks."
        },
        {
            "meal_plan_id": 5,
            "vegetarian": "Use tofu scramble instead of eggs. Plant-based butter and milk alternatives.",
            "easy_options": "Pre-chopped spinach, frozen toast, egg substitute products."
        },
        {
            "meal_plan_id": 6,
            "vegetarian": "Replace turkey with plant-based deli slices or hummus. Use avocado as the main protein source.",
            "easy_options": "Pre-made wraps, baby carrots, pre-sliced vegetables."
        },
        {
            "meal_plan_id": 7,
            "vegetarian": "This meal is already vegetarian! Consider adding nutritional yeast for extra flavor.",
            "easy_options": "Pre-cooked brown rice, frozen stir-fry vegetable mix, pre-pressed tofu."
        },
        {
            "meal_plan_id": 8,
            "vegetarian": "Use plant-based cottage cheese alternatives. Add nuts or seeds for extra protein.",
            "easy_options": "Single-serving cottage cheese cups, pre-cut pineapple, ready-to-eat fruit bowls."
        }
    ]
    
    for swap in seed_swaps:
        Swaps.objects.get_or_create(**swap)
    print("✅ Swaps seeded successfully.")


def seed_hydration_info():
    hydration_infos = [
        {
            "meal_plan_id": 1,
            "hydration": "Drink water throughout the day, aiming for at least 2 liters. Include herbal teas and infused water for variety."
        },
        {
            "meal_plan_id": 2,
            "hydration": "Aim for 3 liters of water daily. Consider electrolyte drinks post-workout to replenish lost minerals."
        },
        {
            "meal_plan_id": 3,
            "hydration": "Consume at least 3.5 liters of water, especially before, during, and after long training sessions."
        },
        {
            "meal_plan_id": 4,
            "hydration": "Ensure you drink 2.5 liters of water daily. Herbal teas and water-rich fruits can help maintain hydration."
        },
        {
            "meal_plan_id": 5,
            "hydration": "Aim for 2.5 liters of water each day. Include a mix of plain water and flavored water with lemon or cucumber."
        },
        {
            "meal_plan_id": 6,
            "hydration": "Drink at least 2 liters of water daily. Coconut water can be a good option for hydration with added electrolytes."
        },
        {
            "meal_plan_id": 7,
            "hydration": "Target 2.5 liters of water per day. Herbal teas and water-rich vegetables can contribute to your hydration needs."
        },
        {
            "meal_plan_id": 8,
            "hydration": "Ensure a daily intake of 2.5 liters of water. Infused waters with fruits or herbs can make hydration more enjoyable."
        }
    ]
    for hydration in hydration_infos:
        Hydration.objects.get_or_create(**hydration)
    print("✅ Hydration info seeded successfully.")


def seed_progress_history():
    seed_progress_histories = [
        {
            "user_id": 1,
            "tips": "Stay consistent with your workouts 🏋️‍♀️ and always maintain a balanced diet 🍏. Remember, progress takes time, so stay patient and dedicated.",
            "differentiate_from_previous": "Increased workout intensity ⚡ by adding more sets and reps, and improved diet quality by focusing on lean proteins 🥩 and fresh vegetables 🥦.",
            "current_analysis": "Notable muscle gain 💪🏽 and significant fat loss 🔥 observed, indicating that the current regimen is effectively working.",
            "status": "On Track 🚀",
            "previous_image": "/media/progress_images/1.jpg",
            "current_image": "progress_images/2.jpg"
        },
        {
            "user_id": 1,
            "tips": "Incorporate more cardio sessions 🏃‍♀️ to enhance fat loss, improve heart health ❤️, and increase overall stamina.",
            "differentiate_from_previous": "Added regular cardio workouts 🏃‍♂️ to the routine, including high-intensity interval training (HIIT) and long-distance running.",
            "current_analysis": "Improved cardiovascular endurance 💓 and slight weight loss 🏋️‍♀️, with visible improvements in stamina and overall fitness levels.",
            "status": "Improving 🔥",
            "previous_image": "/media/progress_images/2.jpg",
            "current_image": "progress_images/3.jpg"
        },
        {
            "user_id": 1,
            "tips": "Focus on recovery 🛀 and nutrition 🍽 to allow muscle growth and prevent injuries. Don’t skip your rest days!",
            "differentiate_from_previous": "Increased protein intake 🥩 to support muscle recovery and added 1 extra rest day per week to allow full muscle regeneration.",
            "current_analysis": "Significant strength improvements 🏋️‍♂️ and muscle growth 🦵 noticed, with less fatigue and better recovery times.",
            "status": "On Fire 🔥💯",
            "previous_image": "/media/progress_images/3.jpg",
            "current_image": "progress_images/4.jpg"
        },
        {
            "user_id": 1,
            "tips": "Stay hydrated 💧 and try to avoid processed foods 🍕 to achieve a healthier, leaner body.",
            "differentiate_from_previous": "Focused on reducing sugar intake 🍭 and added more vegetables 🥗 to daily meals while increasing water intake 💦.",
            "current_analysis": "Visible fat reduction and enhanced muscle definition 💪🏽. Skin appears clearer and energy levels have increased throughout the day.",
            "status": "Getting There 🏅",
            "previous_image": "/media/progress_images/5.jpg",
            "current_image": "progress_images/6.jpg"
        },
        {
            "user_id": 1,
            "tips": "Prioritize healthy fats 🥑 in your diet and keep challenging yourself with more intense workouts 🏋️‍♂️.",
            "differentiate_from_previous": "Focused on improving workout intensity with heavier weights 🏋️ and a stricter diet plan, especially for fat loss 🥑.",
            "current_analysis": "Significant improvements in strength 🏋️‍♀️ and fat loss 🔥, and overall body fat percentage has decreased.",
            "status": "Crushing It 💥",
            "previous_image": "/media/progress_images/6.jpg",
            "current_image": "progress_images/7.jpg"
        },
        {
            "user_id": 1,
            "tips": "Keep focusing on balanced meals 🍽, sleep 💤, and stress management 🧘‍♂️. Your body needs rest to recover and grow.",
            "differentiate_from_previous": "Incorporated mindfulness practices 🧘‍♀️ and better sleep habits 🛏, which helped improve workout performance and recovery.",
            "current_analysis": "Notable improvement in overall health 🏃‍♀️, with better mental clarity 🧠 and visible body toning 💪🏽.",
            "status": "On the Rise 🌱",
            "previous_image": "/media/progress_images/7.jpg",
            "current_image": "progress_images/8.jpg"
        }
    ]
    for history in seed_progress_histories:
        ProgressHistory.objects.get_or_create(**history)
    print("✅ Progress histories seeded successfully with detailed insights!")
