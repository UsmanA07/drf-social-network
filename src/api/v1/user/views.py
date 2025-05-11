from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from apps.user.serializers import UserMeSerializer, UserRegisterSerializer
from apps.user.dto.user_dto import UserRegisterDTO
from apps.user.models import ProfileUser
from apps.user.repositories.user_repositories import DjangoUserRepository
from apps.user.services.user_services import UserRegister


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        print(serializer)
        if not serializer.is_valid():
            print(f'not validated')
            return Response(serializer.errors, status=400)
        user_dto = UserRegisterDTO(
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            username=serializer.validated_data['username'],
            phone=serializer.validated_data['phone'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )
        user_register = UserRegister(DjangoUserRepository())
        user_register.execute(user_dto)
        return Response(status=201)
