from django.core.management.base import BaseCommand

from apps.users.seed_data import seed_users



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        seed_users()
        # seed_categories()

        self.stdout.write(self.style.SUCCESS("Seeding completed."))
