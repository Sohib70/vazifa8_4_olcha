from rest_framework import serializers
from rest_framework.exceptions  import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['id','username','email','address','age','password','password2']


    def validate(self, data):
        password = data.get('password',None)
        password2 = data.get('password2', None)

        if password is None and password2 is None:
            raise ValidationError('Parollar tuliq kiritilmadi')
        if password != password2:
            raise ValidationError("Parollar mos emas")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
            address = validated_data['address'],
            age = validated_data['age'],

        )
        return user
