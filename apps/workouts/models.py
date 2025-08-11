from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    
class Workout(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='workouts', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    video = models.FileField(upload_to='workout_videos/')

    def __str__(self):
        return self.title
