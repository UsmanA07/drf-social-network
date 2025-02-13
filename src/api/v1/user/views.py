from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from api.v1.user.serializers import UserAllSerializer
from apps.user.models import ProfileUser
from apps.user.services.user_services import user_register
from config.settings import AUTH_USER_MODEL


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = UserAllSerializer(ProfileUser.objects.all(), many=True)
        print(f' This is user auth\t{AUTH_USER_MODEL}')
        print(f' This is user auth\t{ProfileUser}')
        return Response(serializer.data)

    def post(self, request):
        user_register(request)
        return Response(status=201)
