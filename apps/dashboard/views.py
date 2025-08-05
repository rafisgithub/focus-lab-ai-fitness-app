from django.shortcuts import render, HttpResponse
from apps.subscriptions.models import IncomeReport, Subscription
from apps.users.models import User
from django.utils import timezone
from datetime import datetime
# Create your views here.

def dashboard_callback(request, context):
    now = timezone.now()

    start_of_month = now.replace(day=1)
    total_subscribers = Subscription.objects.count()
    total_new_subscriptions = Subscription.objects.filter(
        created_at__gte=start_of_month,
    )

    income_report = IncomeReport.objects.first()
    total_income = income_report.total_income if income_report else 0

    if now.month == 12:
        start_of_next_month = now.replace(year=now.year + 1, month=1, day=1)
    else:
        start_of_next_month = now.replace(month=now.month + 1, day=1)

    context.update(
        {
            "total_users": User.objects.count(),
            "total_subscriptions": total_subscribers,
            "total_income": total_income,
            "total_new_subscriptions": total_new_subscriptions.count(),
            "current_month_signups": User.objects.filter(
                date_joined__gte=start_of_month,
                date_joined__lt=start_of_next_month
            ).count(),
            "admins": User.objects.filter(is_staff=True).count(),
            "supper_admins": User.objects.filter(is_superuser=True).count(),
            "data": [
                User.objects.filter(
                    date_joined__year=datetime.now().year,
                    date_joined__month=m
                ).count() for m in range(1, 13)
            ]
        }
    )

    return context
