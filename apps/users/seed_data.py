from apps.users.models import User, UserProfile


def seed_users():
    user_data = [
        {
            "email": "rafi.cse.ahmed@gmail.com",
            "password": "12345678",
            "is_staff": True,
            "is_superuser": True,
            "gender": "male",
            "userprofile": {
                "full_name": "App Creator",
                "avatar": "avatars/1.jpg",
            },
        },
        {
            "email": "admin@admin.com",
            "password": "12345678",
            "is_staff": True,
            "is_superuser": True,
            "gender": "male",
            "userprofile": {
                "full_name": "Admin User",
                "avatar": "avatars/1.jpg",
            },
        },
        {
            "email": "user@user.com",
            "password": "12345678",
            "is_staff": False,
            "gender": "male",
            "is_superuser": False,
            "userprofile": {
                "full_name": "User User",
                "avatar": "avatars/2.jpg",
            },
        },
        {
            "email": "user2@user2.com",
            "password": "12345678",
            "is_staff": False,
            "gender": "female",
            "is_superuser": False,
            "userprofile": {
                "full_name": "User User",
                "avatar": "avatars/3.jpg",
            },
        },
        {
            "email": "user3@user3.com",
            "password": "12345678",
            "is_staff": False,
            "gender": "female",
            "is_superuser": False,
            "userprofile": {
                "full_name": "User User",
                "avatar": "avatars/4.jpg",
            },
        },
        {
            "email": "user4@user4.com",
            "password": "12345678",
            "is_staff": False,
            "gender": "male",
            "is_superuser": False,
            "userprofile": {
                "full_name": "User User",
                "avatar": "avatars/5.jpg",
            },
        }
    ]

    for user in user_data:
        user_instance = User.objects.create_user(
            email=user["email"],
            password=user["password"],
            is_staff=user["is_staff"],
            gender=user["gender"],
            is_superuser=user["is_superuser"],
        )

        UserProfile.objects.create(
            user=user_instance,
            full_name=user["userprofile"]["full_name"],
            avatar=user["userprofile"]["avatar"],
        )

       
    print("✅User data seeded successfully.")