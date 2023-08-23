from rest_framework import serializers
from .models import Product


def validate_title(value):
        queryset = Product.objects.filter(title__iexact=value) ## iexact checks for case sensitive data
        if queryset.exists():
            raise serializers.ValidationError(f"{value} exists")
        return value