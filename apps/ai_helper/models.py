from django.db import models
from apps.users.models import User
# Create your models here.
class SuggestedQuestion(models.Model):
    question =  models.CharField(max_length=1200, blank=True, null=True)

    def __str__(self):
        return self.question

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_history')
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    profile_photo = models.ImageField(upload_to='resumes/profile_photos/', null=True, blank=True)
    goal = models.CharField(max_length=400)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    job_title = models.CharField(max_length=100)
    about = models.TextField()
    linked_in_profile = models.URLField(null=True, blank=True)
    xing_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    still_working_here = models.BooleanField(default=False)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    institute_name = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_enrolled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.degree} at {self.institute_name}"


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill


class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.language} - {self.level}"


class CourseAndTrainingDetail(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='courses_and_training_details')
    name_of_institute = models.CharField(max_length=150)
    course_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.course_name
    


class CoverLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    dob = models.DateField()
    job_title = models.CharField(max_length=255)
    about = models.TextField()

    linked_in_profile = models.URLField(null=True, blank=True)
    xing_profile = models.URLField(null=True, blank=True)

    applying_for = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    hiring_manager_name = models.CharField(max_length=255)

    resume_content = models.TextField(null=True, blank=True)

    why_do_you_want_this_job = models.TextField()
    relevant_experience_or_skill_for_this_role = models.TextField()
    specific_achievement_or_project_to_highlight = models.TextField()
    keywords_or_values_to_emphasize = models.TextField()

    language = models.CharField(max_length=50)

    def __str__(self):
        return f"CoverLetter for {self.first_name} {self.last_name} - {self.company_name}"
