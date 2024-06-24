from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from rest_framework.views import APIView

from .currentUser import CurrentUser
from .models import User
from .serializers import UserSignUpSerializer, UserLoginSerializer, UserSerializer, UserAddressSerializer


class RegistrationView(APIView):
    # permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            address = serializer.validated_data.get('address')
            if invalid_address(address):
                return Response({'answer': 'адрес пользователя не валидный'}, status=status.HTTP_400_BAD_REQUEST, headers={"charset": "utf-8"})
            existing_user = User.objects.filter(email=email).exists()
            if existing_user:
                return Response({'answer': 'Такой пользователь уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(email=email, password=password, first_name=first_name, last_name=last_name, address=address)

            return Response(UserSerializer(user).data, status=status.HTTP_200_OK, headers={"charset": "utf-8"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def invalid_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    loc = geolocator.geocode(address)
    return loc is None


# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class GetUserView(APIView):
    def get(self, request):
        current_user = CurrentUser(request)
        user = current_user.get()
        if user:
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response({'answer': 'пользователь не найден'}, status=status.HTTP_401_UNAUTHORIZED, headers={"charset": "utf-8"})


# class GetUserView(CreateAPIView):
#     def get(self, request, pk):
#         users = User.objects.all()
#         users_out = []
#         for user in products:
#             if product.category.id == int(pk):
#                 products_out.append(product)
#         serializer = ProductSerializer(products_out, many=True)
#         return Response(serializer.data)
#     def get(self, request):
#         user = CurrentUser.get_current_user(request)
#         if user:
#             return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
#         return Response({'answer': 'пользователь не найден'}, status=status.HTTP_401_UNAUTHORIZED, headers={"charset": "utf-8"})


class ChangeUserAddressView(APIView):
    def post(self, request):
        serializer = UserAddressSerializer(data=request.data)
        current_user = CurrentUser(request)
        user = current_user.get()
        if not user:
            return Response({'answer': 'пользователь не залогинен'}, status=status.HTTP_401_UNAUTHORIZED, headers={"charset": "utf-8"})
        if serializer.is_valid():
            address = serializer.validated_data.get('address')
            user.address = address
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            for user in User.objects.all():
                if (password == user.password) and (email == user.email):
                    response = Response(UserSerializer(user).data, status=status.HTTP_200_OK)
                    current_user = CurrentUser(request)
                    current_user.set(user)
                    return response
            return Response({'answer': 'почта/пароль неправильный'}, status=status.HTTP_401_UNAUTHORIZED, headers={"charset": "utf-8"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        current_user = CurrentUser(request)
        current_user.remove()
        return Response(None, status=status.HTTP_200_OK)
