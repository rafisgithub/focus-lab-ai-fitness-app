from .models import  Package, Feature, Subscription
from rest_framework import fields, serializers


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['name']

class SubscriptionPackageSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)
    class Meta:
        model = Package
        fields = ["id","name","stripe_product_id","stripe_price_id","price","type","enabled","features"]


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["id", "name", "price", "type", "enabled"]

class CurrentSubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    class Meta:
        model = Subscription
        fields = ["id", "user", "status", "start_date", "end_date", "pay_per_download_credits", "package"]


