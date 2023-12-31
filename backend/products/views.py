from rest_framework import generics, mixins, authentication, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission
from .mixins import UserQuerySetMixin




######## Class based views

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
    
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

    
    
    
    
    

########### Mixins

class ProductMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, UserQuerySetMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve( request, *args, **kwargs) 
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs) 







class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_create(self, serializer):
        serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer. validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer. save(user=self.request.user, content=content)
        
    # def get_queryset (self, *args, **kwargs):
    #     qs = super () . get_queryset (*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user. is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)




    
    
    
    
############ Function based views
    
@api_view (['GET',"POST" ])
def product_alt_view( request, pk=None, *args, **kwargs) :
    
    method = request.method
    
    if method == 'POST':
        serializer = ProductSerializer (data=request.data)
        
        if serializer.is_valid (raise_exception=True):
            title = serializer. validated_data.get ('title')
            content = serializer.validated_data.get ('content') or None
            
            if content is None:
                content = title
                serializer.save (content=content)
                
                return Response (serializer.data)
            
        return Response ({"invalid": "not good data"}, status=400)
        
    if method == 'GET':
        
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer (obj, many=False). data
            return Response()
        
        queryset = Product.objects.all()
        data = ProductSerializer (queryset, many=True).data
        
        return Response (data)