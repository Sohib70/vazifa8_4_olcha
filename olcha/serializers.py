from rest_framework import serializers
from olcha.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
