from rest_framework import serializers
from .models import Client 


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
                "created_at",
                "created_by",
            ),
        fields = '__all__'