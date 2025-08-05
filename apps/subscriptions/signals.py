import os
import stripe
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone
from .models import Package
from django.db.models.signals import post_save, pre_delete

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@receiver(post_save, sender=Package)
def create_stripe_product(sender, instance, created, **kwargs):
    if not instance.stripe_product_id:
        stripe_product = stripe.Product.create(
            name=instance.name,
            description=f"{instance.name} subscription package",
        )
        instance.stripe_product_id = stripe_product.id
        instance.save()
    if not instance.stripe_price_id:
        if(instance.type == instance.PackageType.PAY_PER_DOWNLOAD):
            stripe_price = stripe.Price.create(
                product=instance.stripe_product_id,
                currency='USD',
                unit_amount=int(instance.price * 100),
            )
        else:
            stripe_price = stripe.Price.create(
                product=instance.stripe_product_id,
                currency= 'USD',
                unit_amount= int(instance.price * 100),
                recurring={
                    'interval': instance.type,
                }
            )
        instance.stripe_price_id = stripe_price.id
        instance.save()


@receiver(post_save, sender=Package)
def update_stripe_product(sender, instance, created, **kwargs):
    if instance.stripe_product_id and instance.stripe_price_id:
        stripe_product = stripe.Product.retrieve(instance.stripe_product_id)
        stripe_price = stripe.Price.retrieve(instance.stripe_price_id)

        if stripe_product['name'] != instance.name:
            stripe.Product.modify(
                stripe_product.id,
                name=instance.name
            )
        
        if stripe_price['unit_amount'] != int(instance.price * 100):
            stripe.Price.modify(instance.stripe_price_id, active=False)

            if(instance.type == instance.PackageType.PAY_PER_DOWNLOAD):
                new_price = stripe.Price.create(
                    product=instance.stripe_product_id,
                    currency='USD',
                    unit_amount=int(instance.price * 100),
                )
            else:
                new_price = stripe.Price.create(
                    product=instance.stripe_product_id,
                    currency='USD',
                    unit_amount=int(instance.price * 100),
                    recurring={
                        'interval': instance.type,
                    }
                )
            instance.stripe_price_id = new_price.id
            instance.save()


@receiver(pre_delete, sender=Package)
def delete_stripe_product(sender, instance, **kwargs):
    if instance.stripe_product_id:
        stripe.Product.modify(
            instance.stripe_product_id,
            active=False,
        )
        stripe.Price.modify(
            instance.stripe_price_id,
            active=False,
        )