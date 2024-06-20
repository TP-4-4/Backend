from users.models import User

from purrfectbytes import settings
from users.serializers import UserSerializer


class CurrentUser:
    # @staticmethod
    # def set_current_user(request, user):
    #     # print("email found")
    #     # print(user.email)
    #     request.session[settings.USER_SESSION_ID] = user.id

    @staticmethod
    def set_current_user(response, user):
        # print("email found")
        # print(user.email)
        response.set_cookie(settings.USER_SESSION_ID, user.id)

    # @staticmethod
    # def get_current_user(request):
    #     id = request.session.get(settings.USER_SESSION_ID, None)
    #     print("lflf")
    #     print(id)
    #     for user in User.objects.all():
    #         if id == user.id:
    #             print("нашли")
    #             return user

    @staticmethod
    def get_current_user(request):
        id = request.COOKIES.get(settings.USER_SESSION_ID)
        print("lflf")
        print(id)
        for user in User.objects.all():
            if id == str(user.id):
                print("нашли")
                return user
