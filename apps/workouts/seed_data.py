from apps.workouts.models import Category, Workout

def seed_categories():
    categories = [
        "Arms Workout",
        "Back Workout",
        "Biceps Workout",
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
    ]

    for category in categories:
        Category.objects.get_or_create(name=category)

def seed_workouts():
    workouts = [
        {
            "title": "Bicep Curl",
            "category": "Arms Workout",
            "gender": "male",
            "video": "https://example.com/bicep_curl.mp4",
        },
        {
            "title": "Tricep Dip",
            "category": "Arms Workout",
            "gender": "female",
            "video": "https://example.com/tricep_dip.mp4",
        },
       
    ]

    for workout in workouts:
        category = Category.objects.get(name=workout["category"])
        Workout.objects.get_or_create(
            title=workout["title"],
            category=category,
            gender=workout["gender"],
            video=workout["video"],
        )

