from rest_framework import serializers, reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField (read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk', 'url', 'title', 'content', 'price', 'sale_price',
        ]
    # def get_url(self, obj):
    #     request = self.context.get ('request')
    #     if request is None:
    #         return None
    #     return reverse("", kwargs={"pk": obj.pk}, request=request)