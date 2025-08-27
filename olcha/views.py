from django.shortcuts import render
from rest_framework.generics import ListAPIView
from olcha.models import Category
from olcha.serializers import CategorySerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
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
