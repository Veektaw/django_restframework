from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators
from api.serializers import UserPublicSerializer, UserNestedSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source = 'user', read_only=True)
    info = UserNestedSerializer(source = 'user', read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    title = serializers. CharField (validators = [validators.validate_title])
    class Meta:
        model = Product
        fields = [
           'owner', 'info', 'pk', 'url', 'title', 'content', 'price', 'sale_price',
        ]
        
    def validate_title(self, value):
        queryset = Product.objects.filter(title__iexact=value)
        if queryset.exists():
            raise serializers.ValidationError(f"{value} already exists.")
        return value
    
    def get_url(self, obj): ### This attaches the URL to the field
        request = self.context.get ('request')
        if request is None:
            return None
        return reverse("products", kwargs={"pk": obj.pk}, request=request)