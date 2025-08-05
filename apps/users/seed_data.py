from apps.users.models import User, UserProfile, VendorProfile


def seed_users():
    user_data = [
        {
            "email": "admin@admin.com",
            "password": "12345678",
            "is_staff": True,
            "is_superuser": True,
            "is_customer": True,
            "is_vendor": True,
            "userprofile": {
                "first_name": "Admin",
                "last_name": "User",
                "phone": "+1234567890",
                "accepted_terms": True,
                "avatar": "media/avatars/1.png",
            },
        },
        {
            "email": "user@user.com",
            "password": "12345678",
            "is_staff": False,
            "is_superuser": False,
            "is_customer": True,
            "is_vendor": True,
            "userprofile": {
                "first_name": "User",
                "last_name": "User",
                "phone": "+12345678",
                "accepted_terms": True,
                "avatar": "media/avatars/1.png",
            },
        },
        {
            "email": "customer@customer.com",
            "password": "12345678",
            "is_staff": False,
            "is_superuser": False,
            "is_customer": True,
            "is_vendor": False,
            "userprofile": {
                "first_name": "User",
                "last_name": "User",
                "phone": "+12345678",
                "accepted_terms": True,
                "avatar": "media/avatars/1.png",
            },
        },
        {
            "email": "vendor@vendor.com",
            "password": "12345678",
            "is_staff": False,
            "is_superuser": False,
            "is_customer": False,
            "is_vendor": True,
            "userprofile": {
                "first_name": "Vendor",
                "last_name": "User",
                "phone": "+12345678",
                "accepted_terms": True,
                "avatar": "media/avatars/1.png",
            },
        },
    ]

    for user in user_data:
        user_instance = User.objects.create_user(
            email=user["email"],
            password=user["password"],
            is_staff=user["is_staff"],
            is_superuser=user["is_superuser"],
            is_customer=user["is_customer"],
            is_vendor=user["is_vendor"],
        )

        UserProfile.objects.create(
            user=user_instance,
            first_name=user["userprofile"]["first_name"],
            last_name=user["userprofile"]["last_name"],
            phone=user["userprofile"]["phone"],
            accepted_terms=user["userprofile"]["accepted_terms"],
            avatar=user["userprofile"]["avatar"],
        )

        VendorProfile.objects.create(
            user=user_instance,
            gstin="123456789012345",
            phone_number="+1234567890",
            store_name="Vendor Store",
            ac_holder_name="Vendor Account",
            ac_number="123456789012",
            confirm_ac_number="123456789012",
            ifsc_code="IFSC1234",
            bank_name="Vendor Bank",
            business_name="Vendor Business",
            bank_details_confirmed=True,
        )
    print("User data seeded successfully.")