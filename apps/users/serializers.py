# author: GongJichao
# createTime: 2020/8/12 18:37
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    mobile = serializers.CharField(required=True)


    # def create(self, validated_data):
    #     super().create()
    #     print(validated_data)
    #     username = validated_data['username']
    #     password = validated_data['password']
    #     mobile = validated_data['mobile']
    #     user = UserProfile(username=username, mobile=mobile)
    #     user.password = make_password(password)
    #     # user.set_password(password)
    #     user.save()
    #     return user

    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ['username', 'password', 'mobile']


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
