from rest_framework import generics, permissions, status
from rest_framework.response import Response

from users.api import serializers
from users.models import User


class SelfView(generics.GenericAPIView):
    serializer_class = serializers.DetailSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def get_object(self):
        return self.get_queryset().get(pk=self.request.user.pk)

    def get(self, request):
        user = self.get_object()
        serializer = self.get_serializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = (permissions.AllowAny, )


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def get_object(self):
        return self.get_queryset().get(pk=self.request.user.pk)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)
