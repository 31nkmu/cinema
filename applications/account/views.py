from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from applications.account.serializers import RegisterSerializer

User = get_user_model()


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
