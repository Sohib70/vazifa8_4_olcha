from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from olcha.models import Category,Product
from olcha.serializers import CategorySerializer,ProductSerializer,ProductDetailSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from users.user_permission import WorkingHoursPermission,WeekdayPermission
# Create your views here.

class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull = True )
        return queryset

class SubcategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        parent_slug = self.kwargs['parent_slug']
        parent_category = Category.objects.get(slug = parent_slug)
        return parent_category.children.all()


class ProductListApiview(ListAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [WorkingHoursPermission]
    authentication_classes = []



class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [WeekdayPermission]
    authentication_classes = []

