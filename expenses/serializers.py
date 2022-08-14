from .models import expense
from rest_framework import serializers


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = expense
        fields = ['id', 'date', 'description', 'amount', 'category']