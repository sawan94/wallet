from users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email')

class UsersCreateSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UsersCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	
	class Meta:
		fields = ['email', 'password']

	def create(self, validated_data):
		email = validated_data.get('email')
		user = authenticate(**validated_data)
		if user:
			return user
		else:
			raise serializers.ValidationError("Invalid email or password")

