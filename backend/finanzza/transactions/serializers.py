from rest_framework import serializers, fields
from django.contrib.auth.models import User
from .models import Transaction


# Transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Transaction
        fields = ('id', 'description', 'amount', 'category',
                  'created_at', 'updated_at', 'is_activated', 'user')
