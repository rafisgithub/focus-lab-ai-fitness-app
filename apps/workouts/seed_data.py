from apps.workouts.models import Category, Workout

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