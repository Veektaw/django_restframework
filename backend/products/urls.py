from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="products"),
    # path('', views.ProductCreateAPIView.as_view()),
    # path('product', views.ProductListAPIView.as_view()),
    path('<int:pk>/', views.product_alt_view),
    # path('', views.product_alt_view),
    path('', views.ProductMixinView.as_view(), name="products"),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    # path('<int:pk>/delete', views.ProductDeleteAPIView.as_view()),
    # path('<int:pk>/update', views.ProductUpdateAPIView.as_view())
]