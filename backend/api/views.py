from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    
    "This gets the products at random"
    
    instance = Product.objects.all().order_by("?").first()
    data = {}
    
    if instance:
        data = ProductSerializer(instance).data
    
    return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    
    "This gets the products at random"

    
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True): # The exception will show you what field is failing
        serializer.save()
        data = serializer.data

        return Response(data)
    return Response({" invalid": "not good data"}, status=400)
 