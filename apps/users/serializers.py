from .models import User, UserProfile
from rest_framework import fields, serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta


class SignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=255, write_only=True)
    last_name = serializers.CharField(required=True, max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        try:
            validate_password(value)
            # return value
        except:
            raise serializers.ValidationError("Password is not valid")
        return value

    def create(self, validated_data):

        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")

        if validate_password(validated_data["password"]) == None:
            password = make_password(validated_data["password"])
            user = User.objects.create(
                # username=validated_data['username'],
                email=validated_data["email"],
                password=password,
            )

            UserProfile.objects.create(
                user=user, first_name=first_name, last_name=last_name
            )
        return user


#  user
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        ]


# UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "phone_number",
        ]

        read_only_fields = ["user"]


# forgot password


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        # Generate OTP and send via email
        user.generate_otp()
        send_mail(
            "Password Reset OTP",
            f"Your OTP for password reset is {user.otp}",
            "noreply@example.com",  # Change this to your email
            [user.email],
            fail_silently=False,
        )
        return value


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "User not found."})

        # Check if OTP is correct and not expired
        if user.otp != data["otp"]:
            raise serializers.ValidationError({"otp": "Invalid OTP."})

        if user.otp_exp < now():  # OTP expired
            raise serializers.ValidationError({"otp": "OTP expired."})

        # Mark OTP as verified
        user.otp_verified = True
        user.save()

        return data


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "User not found."})

        # Check if OTP was verified
        if not user.otp_verified:
            raise serializers.ValidationError({"otp": "OTP verification required."})

        return data

    def save(self, **kwargs):
        user = User.objects.get(email=self.validated_data["email"])
        user.set_password(self.validated_data["new_password"])
        user.otp = None  # Clear OTP after successful reset
        user.otp_exp = None
        user.otp_verified = False  # Reset verification status
        user.save()
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "phone_number", "user"]

        extra_kwargs = {
            "user": {"read_only": True}
        }


class ProfileUpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["profile_image", "user"]

        
        extra_kwargs = {
            "user": {"read_only": True}
        }
