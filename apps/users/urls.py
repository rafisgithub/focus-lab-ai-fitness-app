from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    SignupAPIView,
    # SigninAPIView,
    UserDetail,
    UserProfileList,
    UserProfileDetail,
    PasswordResetRequestAPIView,
    OTPVerificationAPIView,
    PasswordResetAPIView,
    ProfileUpdateAPIView,
    ProfileUpdateImageAPIView,
)

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="signup"),
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    #  user delete
    path("user/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    #  user profile
    path("user/profile/", UserProfileList.as_view(), name="user_profile_list"),
    path("user/profile/<int:pk>/",UserProfileDetail.as_view(), name="user_profile_detail",),
    # forgot password
    path("password-reset/request/", PasswordResetRequestAPIView.as_view(), name="password-reset-request",),
    path("password-reset/verify-otp/", OTPVerificationAPIView.as_view(), name="password-reset-verify-otp",),  # New API
    path("password-reset/change-password/",PasswordResetAPIView.as_view(),name="password-reset-change",),

    path("update-profile/",ProfileUpdateAPIView.as_view(),name="update-profile",),
    path("update-profile-image/", ProfileUpdateImageAPIView.as_view(), name="update-profile-image"),
]
