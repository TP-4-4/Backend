from purrfectbytes import settings
from users.models import User


class CurrentUser:
    def __init__(self, request):
        self.session = request.session
        current_user = self.session.get(settings.USER_SESSION_ID)
        if not current_user:
            current_user = self.session[settings.USER_SESSION_ID] = {}
        self.current_user = current_user

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def set(self, user):
        user_id = str(user.id)
        if user_id not in self.current_user:
            self.current_user[user_id] = user.email
        self.save()

    def get(self):
        if len(self.current_user) == 0:
            return None
        user_email = list(self.current_user.values())[0]
        return User.objects.filter(email=user_email)[0]

    def remove(self):
        if len(self.current_user) != 0:
            del self.session[settings.USER_SESSION_ID]
            self.save()


    # @staticmethod
    # def set_current_user(request, user):
    #     # print("email found")
    #     # print(user.email)
    #     request.session[settings.USER_SESSION_ID] = user.id
    #     request.session.modified = True

    # @staticmethod
    # def set_current_user(response, user):
    #     # print("email found")
    #     # print(user.email)
    #     response.set_cookie(settings.USER_SESSION_ID, user.id)

    # @staticmethod
    # def get_current_user(request):
    #     id = request.session.get(settings.USER_SESSION_ID, None)
    #     print("lflf")
    #     print(id)
    #     for user in User.objects.all():
    #         if id == user.id:
    #             print("нашли")
    #             return user

    # @staticmethod
    # def get_current_user(request):
    #     id = request.COOKIES.get(settings.USER_SESSION_ID)
    #     print("lflf")
    #     print(id)
    #     for user in User.objects.all():
    #         if id == str(user.id):
    #             print("нашли")
    #             return user
