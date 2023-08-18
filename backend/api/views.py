from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    
    "This gets the products at random"
    
    instance = Product.objects.all().order_by("?").first()
    data = {}
    
    if instance:
        data = ProductSerializer(instance).data
    
    return Response(data)

 