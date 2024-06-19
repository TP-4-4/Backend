from users.models import User

from purrfectbytes import settings
from users.serializers import UserSerializer


class CurrentUser:
    @staticmethod
    def set_current_user(request, user):
        print("email found")
        print(user.email)
        request.session[settings.USER_SESSION_ID] = user.email

    @staticmethod
    def get_current_user(request):
        email = request.session[settings.USER_SESSION_ID]
        print("lflf")
        print(email)
        for user in User.objects.all():
            if email == user.email:
                print("нашли")
                return user
