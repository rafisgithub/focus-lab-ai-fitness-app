from django.conf import settings
from django.db import models
from django.utils.translation import get_language
from django.utils import timezone


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        lang = get_language()
        if lang == 'de':
            return self.name_de or self.name
        return self.name_en or self.name

class Package(models.Model):

    class PackageType(models.TextChoices):
        MONTHLY = 'month', 'Monthly'
        PAY_PER_DOWNLOAD = 'pay_per_download', 'Pay Per Download'

    features = models.ManyToManyField(Feature, blank=True, related_name='packages')
    name = models.CharField(max_length=100, blank=True, null=True)
    stripe_product_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(
        max_length=20,
        choices=PackageType.choices,
        default=PackageType.MONTHLY  # Optional: default value
    )
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.get_type_display()} - {self.price} USD"


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    package = models.ForeignKey(Package, on_delete=models.PROTECT, blank=True, null=True)
    pay_per_download_credits = models.IntegerField(default=0)
    stripe_subscription_id = models.CharField(max_length=100, blank=True, null=True) 
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending')
    ], default='pending')  
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_subscription(self):
        return self.status == 'active' and self.end_date > timezone.now()
    def has_pay_per_download_credits(self):
       return self.pay_per_download_credits > 0
    
    def __str__(self):
        return f"{self.user.email} "
    

class PaymentHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_gateway = models.CharField(max_length=50, choices=[
        ('stripe', 'Stripe'),
        ('paypal', 'PayPal'),
    ])
    payment_status = models.CharField(max_length=20, choices=[
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ])
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.package.name}"
    
class IncomeReport(models.Model):
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Income Report for {self.month.strftime('%B %Y')} - Total Income: {self.total_income}"