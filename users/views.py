from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSignUpSerializer, UserLoginSerializer, UserSerializer


class RegistrationView(CreateAPIView):
    # permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            existing_user = User.objects.filter(email=email).exists()
            if existing_user:
                return Response({'answer': 'Такой пользователь уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(email=email, password=password)

            return Response(UserSerializer(user).data, status=status.HTTP_200_OK, headers={"charset": "utf-8"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(CreateAPIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        for user in User.objects.all():
            if (password == user.password) and (email == user.email):
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response({'answer': 'почта/пароль неправильный'}, status=status.HTTP_401_UNAUTHORIZED, headers={"charset": "utf-8"})
