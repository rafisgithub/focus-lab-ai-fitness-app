from apps.users.models import User, UserProfile

def seed_users():
    User.objects.all().delete()

    data = [
        {
            'first_name': 'Admin',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'User',
            'phone_number': '1234567890',
            'email': 'admin@admin.com',
            'password': '12345678',
            'is_superuser': True,
            'is_staff': True,
        },
        {   
            'first_name': 'User',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'User',
            'phone_number': '1234567890',
            'email': 'user@user.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Rafi',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Ahmed',
            'phone_number': '1234567890',
            'email': 'rafi.cse.ahmed@gmail.com',
            'password': '12345678',
            'is_superuser': True,
            'is_staff': True,
        },
    {
            'first_name': 'Lukas',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Schmidt',
            'phone_number': '1234567890',
            'email': 'lukas.schmidt@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Anna',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Müller',
            'phone_number': '1234567890',
            'email': 'anna.mueller@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Felix',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Weber',
            'phone_number': '1234567890',
            'email': 'felix.weber@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Sophie',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Schneider',
            'phone_number': '1234567890',
            'email': 'sophie.schneider@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Jonas',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Fischer',
            'phone_number': '1234567890',
            'email': 'jonas.fischer@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Laura',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Wagner',
            'phone_number': '1234567890',
            'email': 'laura.wagner@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Tim',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Becker',
            'phone_number': '1234567890',
            'email': 'tim.becker@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Marie',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Hoffmann',
            'phone_number': '1234567890',
            'email': 'marie.hoffmann@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Niklas',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Koch',
            'phone_number': '1234567890',
            'email': 'niklas.koch@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
        {
            'first_name': 'Lea',
            'profile_image' : 'user-profiles/1.png',
            'last_name': 'Richter',
            'phone_number': '1234567890',
            'email': 'lea.richter@example.com',
            'password': '12345678',
            'is_superuser': False,
            'is_staff': False,
        },
    ]

    for item in data:
        user = User.objects.create_user(
            email=item['email'],
            password=item['password'],
            is_superuser=item['is_superuser'],
            is_staff=item['is_staff']
        )
        UserProfile.objects.create(
            user=user,
            first_name=item['first_name'],
            last_name=item['last_name'],
            phone_number=item['phone_number'],
            profile_image=item['profile_image']
        )

    print("✅ Users seeded successfully.")
