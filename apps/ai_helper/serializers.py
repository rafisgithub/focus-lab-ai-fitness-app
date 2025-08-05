"""Module providing serializers for the AI helper app."""
from rest_framework import serializers
from .models import ChatHistory, CoverLetter, SuggestedQuestion, Resume, WorkExperience, Education, Skill, Language, CourseAndTrainingDetail


class SuggestedQuestionSerializer(serializers.ModelSerializer):
    """Serializer for SuggestedQuestion model."""

    class Meta:
        """Meta class for SuggestedQuestionSerializer."""
        model = SuggestedQuestion
        fields = ("question",)

class ChatHistorySerializer(serializers.ModelSerializer):
    """Serializer for ChatHistory model."""

    class Meta:
        """Meta class for ChatHistorySerializer."""
        model = ChatHistory
        fields = ("user", "question", "answer", "created_at")


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company_name', 'start_date', 'end_date', 'still_working_here', 'responsibilities']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['institute_name', 'degree', 'start_date', 'end_date', 'currently_enrolled']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language', 'level']


class CourseAndTrainingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAndTrainingDetail
        fields = ['course_name', 'name_of_institute','course_name', 'start_date', 'end_date']


class ResumeSerializer(serializers.ModelSerializer):
    work_experiences = WorkExperienceSerializer(many=True)
    educations = EducationSerializer(many=True)
    skills = SkillSerializer(many=True)
    languages = LanguageSerializer(many=True)
    courses_and_training_details = CourseAndTrainingDetailSerializer(many=True)
    
    class Meta:
        model = Resume
        fields = ['goal', 'profile_photo', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'dob', 'job_title', 'about', 'linked_in_profile', 'xing_profile','work_experiences', 'educations', 'skills', 'languages', 'courses_and_training_details']

    def create(self, validated_data):
        work_experiences = validated_data.pop('work_experiences')
        educations = validated_data.pop('educations')
        skills = validated_data.pop('skills')
        languages = validated_data.pop('languages')
        courses = validated_data.pop('courses_and_training_details')

        resume = Resume.objects.create(**validated_data, user=self.context['request'].user)

        for exp in work_experiences:
            WorkExperience.objects.create(resume=resume, **exp)

        for edu in educations:
            Education.objects.create(resume=resume, **edu)

        for skill in skills:
            Skill.objects.create(resume=resume, **skill)

        for lang in languages:
            Language.objects.create(resume=resume, **lang)

        for course in courses:
            CourseAndTrainingDetail.objects.create(resume=resume, **course)

        return resume



class CoverLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverLetter
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'dob', 'job_title', 'about', 'linked_in_profile', 'xing_profile', 'applying_for', 'company_name', 'company_location', 'hiring_manager_name', 'why_do_you_want_this_job', 'relevant_experience_or_skill_for_this_role', 'specific_achievement_or_project_to_highlight', 'keywords_or_values_to_emphasize','resume_content']