from django.db import models

from apps.users import serializers
from apps.users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    
class Workout(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'male_and_female', 'Male and Female'

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='workouts', on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=Gender.choices)
    video = models.FileField(upload_to='workout_videos/')

    def __str__(self):
        return self.title


class SuggestedWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# Meal Plan Model
class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.TextField()
    calories = models.TextField()
    hydration = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Meal Plan"

# Macros Model
class Macros(models.Model):
    meal_plan = models.OneToOneField(MealPlan, on_delete=models.CASCADE, related_name='macros_info')
    protein = models.TextField()
    carbs = models.TextField()
    fat = models.TextField()
    fiber = models.TextField()

    def __str__(self):
        return f"Macros for {self.meal_plan.user.username}"

# Meal Model
class Meal(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='meals')
    meal = models.TextField()
    items = models.TextField()
    approx_kcal = models.TextField()
    protein_g = models.TextField()

    def __str__(self):
        return f"{self.meal} for {self.meal_plan.user.username}"

# Swaps Model
class Swaps(models.Model):
    meal_plan = models.OneToOneField(MealPlan, on_delete=models.CASCADE, related_name='swaps_info')
    vegetarian = models.TextField()
    easy_options = models.TextField()

    def __str__(self):
        return f"Swaps for {self.meal_plan.user.username}"

# Hydration Model
class Hydration(models.Model):
    meal_plan = models.OneToOneField(MealPlan, on_delete=models.CASCADE, related_name='hydration_info')
    hydration = models.TextField()

    def __str__(self):
        return f"Hydration info for {self.meal_plan.user.username}"

# Optional UserMealPlan Association Model
class UserMealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'meal_plan')

    def __str__(self):
        return f"{self.user.username} - {self.meal_plan.id}"
