from django.core.management.base import BaseCommand
from apps.subscriptions.seed_data import (
    seed_subscription_features,
    seed_subscription_packages,
)
from apps.users.seed_data import seed_users
from apps.cms.seed_data import (
    how_it_work_feature_seed,
    seed_brands,
    seed_faqs,
    seed_features,
    seed_footer,
    seed_testimonials,
    seed_benefits,
    seed_pages,
    seed_hero_section,
    how_it_work_seed,
    seed_interview_coach_section,
    seed_interview_coach_section,
    seed_upcoming_feature_interested_user,
    seed_global_cta
)
from apps.ai_helper.seed_data import seed_suggested_questions, seed_chat_history


class Command(BaseCommand):
    help = "Seed data for users and brands"

    def handle(self, *args, **kwargs):
        seed_users()
        # seed_hero_section()
        # seed_brands()
        # seed_features()
        # seed_testimonials()
        # seed_benefits()
        # seed_subscription_features()
        # seed_subscription_packages()
        # seed_faqs()
        # seed_suggested_questions()
        # seed_pages()
        # seed_chat_history()
        # how_it_work_feature_seed()
        # how_it_work_seed()
        # seed_interview_coach_section()
        # seed_footer()
        # seed_upcoming_feature_interested_user()
        # seed_global_cta()
        self.stdout.write(self.style.SUCCESS("Seeding completed."))
