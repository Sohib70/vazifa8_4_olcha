from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import permissions,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView

class RegisterApi(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self,request):
        data = request.data
        password = data['password']
        password2 = data['password2']
        if password != password2:
            raise ValidationError('Parollar mos emas!')
        username = data['username']
        email = data['email']
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return Response({'msg':"Ruyxatdan o'tildi!",'status':status.HTTP_201_CREATED})


class LoginApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        data = request.data
        email = data['email']
        password = data['password']

        if not CustomUser.objects.filter(email=email).exists():
            return Response({'error':"Bunaqa loginli foydalanuvchi mavjud emas",
                             'status':status.HTTP_400_BAD_REQUEST})

        user = authenticate(email=email,password=password)
        token = RefreshToken.for_user(user)

        data = {
            'refresh':str(token),
            'access':str(token.access_token),
            'status':status.HTTP_200_OK
        }
        return Response(data=data)

class LogoutApi(APIView):
    def post(self,request):
        data = request.data
        try:
            token = RefreshToken(data['refresh'])
            token.blacklist()
            return Response({"msg":"Chiqdingiz!",'status':status.HTTP_200_OK})
        except Exception as e:
            return Response({'error':str(e),'status':status.HTTP_400_BAD_REQUEST})


class TokenRefresh(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        data = request.data
        try:
            token = RefreshToken(data['refresh'])
            return Response({"access":str(token.access_token),'status':status.HTTP_201_CREATED})
        except Exception as e:
            return Response({'error':str(e),'status':status.HTTP_400_BAD_REQUEST})