# author: GongJichao
# createTime: 2020/8/12 18:37
from rest_framework import serializers

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
