from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import UserProfile
from users.serializers import UserSerializer, LoginSerializer


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):

    queryset = []
    serializer_class = UserSerializer

    # def get_serializer_class(self):
    #     if self.login.__name__ == 'login':
    #         print('login')
    #         return LoginSerializer
    #     else:
    #         print('user')
    #         return UserSerializer

    def existed(self, request, username):
        user_name = UserProfile.objects.filter(username=username).all()

        if user_name:
            return Response({
                'data': True,
                'code': Response.status_code
            })
        return Response({
            'data': False,
            'code': Response.status_code
        })

    # @action(methods=['post'], detail=False)
    def register(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        username = serializer.data['username']
        password = serializer.data['password']
        mobile = serializer.data['mobile']
        user = UserProfile(username=username, mobile=mobile)
        # 加密
        user.password = make_password(password)
        user.last_login = timezone.now()
        user.save()

        return Response({
            'data': serializer.data,
            'code': Response.status_code
        })


class LoginViewSet(GenericViewSet):

    queryset = []
    serializer_class = LoginSerializer

    # 登录或其他用处是用户登录验证
    # query_result = User.objects.filter(Q(email=username) | Q(username=username))
    #
    # # 查询时密码是加密后
    # user = auth.authenticate(username=query_result[0].username, password=password)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data['username']
        password = serializer.data['password']
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                user.last_login = timezone.now()
                user.save()
                return Response({
                    'data': serializer.data,
                    'code': 200
                })
            else:
                return Response({
                    'data': serializer.data,
                    'code': 400
                })
        except Exception as e:
            print('用户登陆失败', e)
            return Response({
                    'data': serializer.data,
                    'code': 500
                })





