from .models import User, UserProfile
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.urls import reverse_lazy
from django.db.models import Count
import json
from django.db.models.functions import TruncDate
from rest_framework.validators import ValidationError
from .serializers import (
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
    ChangePasswordSerializer,
    SendOTPSerializer,
    ResendOTPSerializer,
    UpdateProfileAvatarSerializer,
    VerifyOTPSerializer,
    ResetPasswordSerializer,
    UserProfileSerializer,
)
from django.http import Http404
from apps.utils.helpers import success, error


# Create your views here.
class SignUpView(APIView):
    permission_classes = []

    def post(self, request):

        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=serializer.data,message="User created successfully.",code=status.HTTP_201_CREATED)
        raise ValidationError(serializer.errors)

class SignInView(APIView):

    permission_classes = []

    def post(self, request):
        
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            return success(data=serializer.data, message="Signin successful.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class SignOutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = SignOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="Logout successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="Password changed successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class SendOTPView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            return success(data=[], message="OTP sent to email successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class ResendOTPView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
        if serializer.is_valid():
            return success(data=[], message="OTP resent successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class VerifyOTPView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="OTP verified successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)

class ResetPasswordView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="Password reset successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class UpdateProfileAvatarView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request):
        user = request.user

        try:
            userProfile = UserProfile.objects.select_related('user').get(user=user)
        except UserProfile.DoesNotExist as e:
            return error(message="User profile not found.", errors=e, code=status.HTTP_400_BAD_REQUEST)

        serializer = UpdateProfileAvatarSerializer(userProfile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success(data=serializer.data, message="Profile avatar updated successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request):
        user = request.user

        try:
            userProfile = UserProfile.objects.select_related('user').get(user=user)
        except UserProfile.DoesNotExist:
            return error(message="User profile not found.", code=status.HTTP_400_BAD_REQUEST)

        serializer = UserProfileSerializer(userProfile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success(data=serializer.data, message="Profile updated successfully.", code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)


class ProfileGet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user

        try:
            profile = UserProfile.objects.select_related('user').get(user=user)
        except UserProfile.DoesNotExist:
            return error(message="User profile not found.", code=status.HTTP_400_BAD_REQUEST)

        data = {
            'id': profile.id,
            'email': profile.user.email,
            'full_name': profile.full_name,
            'accepted_terms': profile.accepted_terms,
            'avatar_url': profile.avatar.url if profile.avatar else None,
            'created_at': profile.created_at,
            'updated_at': profile.updated_at,
        }
        return success(data=data, message="Profile retrieved successfully.", code=status.HTTP_200_OK)


def dashboard_callback(request, context):
    from .models import User

    total_user = User.objects.count()

    user_join_data = (
        User.objects
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    labels = [entry['date'].strftime('%b %d') for entry in user_join_data]
    data = [entry['count'] for entry in user_join_data]

    context.update({
        "total_user": total_user,
        "labels": json.dumps(labels),
        "data": json.dumps(data),
    })

    return context

