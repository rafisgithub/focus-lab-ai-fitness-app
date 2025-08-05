from .models import Contact
from rest_framework import fields, serializers

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message', 'agree_terms']

    def validate(self, attrs):
        if not attrs.get('agree_terms'):
            raise serializers.ValidationError({"agree_terms": "You must agree to the terms and conditions."})
        return attrs