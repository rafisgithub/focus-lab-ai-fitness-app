from .models import Benefit, Brand, Faq, Feature, GlobalCta, HeroSection, HowItWork, InterviewCoachSection, Page, Testimonial, Footer
from rest_framework import fields, serializers



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("name", "logo")


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "title", "short_description", "logo"
    

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "name", "user_image", "profession", "rating", "comment"


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = "title", "sub_title", "logo"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "question", "answer", "is_active"


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "title", "content", "type", "is_active"


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ("title", "sub_title", "banner")


class HowItWorkSerializer(serializers.ModelSerializer):
    features = serializers.StringRelatedField(many=True)

    class Meta:
        model = HowItWork
        fields = ["title", "sub_title", "short_description", "side_image", "features"]

class InterviewCoachSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewCoachSection
        fields = ("title", "short_description")


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer 
        fields = ("content", "copyright_text")


class GlobalCtaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalCta
        fields = ("title", "description", "button_text")