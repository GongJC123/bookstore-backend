from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import UserProfile
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    # @action(methods=['get'], detail=False, url_path='<str:username>')
    def existed(self, request):
        username = self.kwargs.get('username')
        print('user==============', username)
        user_name = UserProfile.objects.get(username=username)
        if user_name:
            return Response({
                'data': True,
                'code': Response.status_code
            })
        return Response({
            'data': False,
            'code': Response.status_code
        })


