from rest_framework import serializers
from ..models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email', 'message', 'created_at']
        extra_kwargs = {
            'created_at': {"read_only": True}
        }
