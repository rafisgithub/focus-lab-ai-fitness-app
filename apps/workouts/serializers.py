from rest_framework import serializers
from .models import Category, ProgressHistory, SuggestedWorkout, Workout,MealPlan, Macros, Meal, Swaps, Hydration, UserMealPlan


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class WorkoutSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Workout
        fields = "__all__"



class MacrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macros
        fields = ['protein', 'carbs', 'fat', 'fiber']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['meal', 'items', 'approx_kcal', 'protein_g']


class SwapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swaps
        fields = ['vegetarian', 'easy_options']


class HydrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydration
        fields = ['hydration']


class MealPlanSerializer(serializers.ModelSerializer):
    macros_info = MacrosSerializer(read_only=True)
    meals = MealSerializer(many=True, read_only=True)
    swaps_info = SwapsSerializer(read_only=True)
    hydration_info = HydrationSerializer(read_only=True)

    class Meta:
        model = MealPlan
        fields = ['id', 'user', 'goal', 'calories', 'hydration', 'notes', 
                  'macros_info', 'meals', 'swaps_info', 'hydration_info','date']
        

class ProgressHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressHistory
        fields = ['id','user','tips','differentiate_from_previous','current_analysis','status','previous_image','current_image','date']