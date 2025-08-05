from django.db import models
from django.utils.translation import get_language

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    def __str__(self):
        return self.name

class Feature(models.Model):
    title = models.CharField(max_length=255, unique=True)
    short_description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='features/', blank=True, null=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    user_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Benefit(models.Model):
    title = models.CharField(max_length=255, unique=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='benefits/', blank=True, null=True)
    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    banner = models.ImageField(upload_to='hero_sections/', blank=True, null=True)

    def __str__(self):
        return self.title

    
class Page(models.Model):
    class Type(models.TextChoices):
        TERMSANDCONDITIONS = 'terms_and_conditions', 'Terms and Conditions'
        PRIVACYPOLICY = 'privacy_policy', 'Privacy Policy'
        IMPRINT = 'imprint', 'Imprint'

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=Type.choices,
    )
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


    
class HowItWorkFeature(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        lang = get_language()
        if lang == 'de':
            return self.name_de or self.name
        return self.name_en or self.name

    def __str__(self):
        return self.name
    
    

class HowItWork(models.Model):
    features = models.ManyToManyField(HowItWorkFeature, related_name='how_it_works')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.TextField()
    side_image = models.ImageField(upload_to='how_it_works/', blank=True, null=True)

    def __str__(self):
        return self.title


class InterviewCoachSection(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()

    def __str__(self):
        return self.title
    
class Footer(models.Model):
    content = models.TextField()
    copyright_text = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return "Footer Content"
    
    

class UpcomingFeatureInterestedUser(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
    

class GlobalCta(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
