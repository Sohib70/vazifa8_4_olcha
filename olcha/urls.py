from .views import CategoryListApiView,SubcategoryListApiView,ProductListApiview,ProductDetailApiView
from django.urls import path

urlpatterns = [
    path('',CategoryListApiView.as_view()),
    path('category/<slug:parent_slug>/',SubcategoryListApiView.as_view()),
    path("products/",ProductListApiview.as_view()),
    path('products/<int:pk>/',ProductDetailApiView.as_view())
]