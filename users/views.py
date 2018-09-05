# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, logout
from rest_framework import generics
from users.models import User
from users.serializers import UsersCreateSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from users.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class CreateUser(generics.CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = UsersCreateSerializer

class UserView(APIView):
    def get(self,request, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		token,created = Token.objects.get_or_create(user=user)
		login(request, user) 
		return Response({"token": token.key, "name": user.get_full_name()})


class LogoutView(APIView):
	def post(self, request, *args, **kwargs):
		logout(request)
		return Response({"message": "Successfully logged out"})