from django.core.management.base import BaseCommand
from ...models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seed the database with sample data'
     
    def handle(self, *args, **kwargs):

        User.objects.all().delete()

        data = [
            {
                'email': 'admin@admin.com',
                'password': make_password('12345678'),
                'is_superuser': True,
                'is_staff': True,
            },
            {
                'email': 'user@user.com',
                'password': make_password('12345678'),
                'is_superuser': False,
                'is_staff': False,

                
            }

        ]

        for item in data:
            User.objects.update_or_create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
