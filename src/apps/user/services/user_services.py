from api.v1.user.serializers import UserRegisterSerializer
# from apps.user.models import ProfileUser


def user_register(request):
    user = UserRegisterSerializer(data=request.data)
    if user.is_valid():
        return user.save()
