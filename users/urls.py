from django.urls import path
from .views import RegistrationView, LoginView, ChangeUserAddressView, GetUserView, LogoutView
app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('details/', GetUserView.as_view(), name='details'),
    path('address/', ChangeUserAddressView.as_view(), name='address'),
]