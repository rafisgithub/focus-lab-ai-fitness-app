import json
from .models import User, UserProfile
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.utils.helpers import success, error
from .serializers import (
    SignupSerializer,
    UserSerializer,
    UserProfileSerializer,
    PasswordResetRequestSerializer,
    OTPVerificationSerializer,
    PasswordResetSerializer,
    ProfileUpdateSerializer,
    ProfileUpdateImageSerializer,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import Http404


# Create your views here.
class SignupAPIView(APIView):

    permission_classes = []

    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": True,
                "status": status.HTTP_201_CREATED,
                "message": "User created successfully",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_error = {
            "success": False,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "User creation failed",
            "data": serializer.errors,
        }
        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)




# # signin 
# class SigninAPIView(TokenObtainPairView):
#     permission_classes = []
    
#     def post(self, request, *args, **kwargs):
#         # serializer = self.get_serializer(data=request.data)
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except ValidationError as e:
#             return Response(
#                 {"success": False, "errors": e.detail},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
        
#         data = {
#             "refresh": serializer.validated_data["refresh"],
#             "access": serializer.validated_data["access"],
#             "user":{
#                 "id": serializer.user.id,
#                 "email": serializer.user.email,
#                 "is_staff": serializer.user.is_staff,
#                 "is_active": serializer.user.is_active,
#                 "date_joined": serializer.user.date_joined.isoformat(),
#             }
#         }
#         response_data = {
#             "success": True,
#             "status": status.HTTP_200_OK,
#             "message": "User signed in successfully",
#             "data": data,
#         }
#         return Response(response_data, status=status.HTTP_200_OK)

# user
class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):

        if not (self.request.user.id == pk):
            response_data = {
                "success": False,
                "status": status.HTTP_403_FORBIDDEN,
                "message": "You are not authorized to delete this user",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        user = self.get_object(pk)
        user.delete()
        response_data = {
            "success": True,
            "status": status.HTTP_204_NO_CONTENT,
            "message": "User deleted successfully",
        }
        return Response(response_data)


# user profile
class UserProfileList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        userProfile = UserProfile.objects.filter(user=self.request.user)
        serializer = UserProfileSerializer(userProfile, many=True)
        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "User profile fetched successfully",
            "data": serializer.data,
        }
        return Response(response_data)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": True,
                "status": status.HTTP_201_CREATED,
                "message": "User profile created successfully",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_error = {
            "success": False,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "User profile creation failed",
            "data": serializer.errors,
        }
        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk, user=self.request.user)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        serializer = UserProfileSerializer(userProfile)
        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "User profile fetched successfully",
            "data": serializer.data,
        }
        return Response(response_data)

    def put(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        serializer = UserProfileSerializer(userProfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "User profile updated successfully",
                "data": serializer.data,
            }
            return Response(response_data)
        response_error = {
            "success": False,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "User profile update failed",
            "data": serializer.errors,
        }
        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        userProfile.delete()
        response_data = {
            "success": True,
            "status": status.HTTP_204_NO_CONTENT,
            "message": "User profile deleted successfully",
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)






# forgot password

class PasswordResetRequestAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {"success": True, "message": "OTP sent to email."}, 
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "errors": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )



class OTPVerificationAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {"success": True, "message": "OTP verified successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )




class PasswordResetAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Password reset successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        profile = request.user.profile

        serializer = ProfileUpdateSerializer(data=request.data, instance=profile)
        if serializer.is_valid():
            serializer.save()
            return success(serializer.data, "Profile updated successfully", status.HTTP_200_OK)
        else:
            return error("Profile update failed", serializer.errors)


class ProfileUpdateImageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        profile = request.user.profile

        if 'profile_image' not in request.data:
            return error("Profile image is required", status.HTTP_400_BAD_REQUEST)

        serializer = ProfileUpdateImageSerializer(data=request.data, instance=profile)
        if serializer.is_valid():
            serializer.save()
            return success(serializer.data, "Profile image updated successfully", status.HTTP_200_OK)
        else:
            return error("Profile image update failed", serializer.errors)

