from django.core.management.base import BaseCommand

from apps.users.seed_data import seed_users
from apps.workouts.seed_data import seed_categories,seed_workouts
from apps.system_setting.seed_data import seed_about_system, seed_pages, seed_social_media, seed_smtp_credentials

class Command(BaseCommand):
    help = "Seed data for users and brands"

    def handle(self, *args, **kwargs):
        seed_users()
        seed_categories()
        seed_workouts()
        seed_about_system()
        seed_social_media()
        seed_smtp_credentials()
        seed_pages()    

        # seed_subscription_features()
        # seed_subscription_packages()
     
        self.stdout.write(self.style.SUCCESS("Seeding completed."))
