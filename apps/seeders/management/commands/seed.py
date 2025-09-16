from django.core.management.base import BaseCommand

from apps.users.seed_data import seed_users
from apps.workouts.seed_data import (
    seed_categories,
    seed_workouts,
    seed_suggested_workouts,
    seed_suggested_meal_plans,
    seed_macros,
    seed_meals,
    seed_swaps,
    seed_hydration_info,
    seed_progress_history
)
from apps.system_setting.seed_data import (
    seed_openai_credentials,
    seed_system_setting,
    seed_social_media,
    seed_smtp_credentials,
    seed_system_color,
)
from apps.cms.seed_data import seed_faq, seed_page


class Command(BaseCommand):
    help = "Seed data for users and brands"

    def handle(self, *args, **kwargs):
        seed_users()
        seed_categories()
        seed_workouts()
        seed_system_setting()
        seed_social_media()
        seed_smtp_credentials()
        seed_system_color()
        seed_page()
        seed_faq()
        seed_openai_credentials()
        seed_suggested_workouts()
        seed_suggested_meal_plans()
        seed_macros()
        seed_meals()
        seed_swaps()
        seed_hydration_info()
        seed_progress_history()

        self.stdout.write(self.style.SUCCESS("Seeding completed."))
