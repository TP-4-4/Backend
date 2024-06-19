from django.db import models


class Courier(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    #birth_date = models.DateField(auto_now_add=True)
    #email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.last_name

    class Meta:
        db_table = "couriers"







# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     last_name = Column(String)
#     first_name = Column(String)
#     middle_name = Column(String)
#     email = Column(String)
#     phone_number = Column(String)
#     birth_date = Column(Date)
#     password = Column(String)
#     orders = relationship("Order", back_populates="user")



# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser):
#     email = models.EmailField(_('email address'), unique=True)
#     last_name = models.CharField(max_length=150)
#     first_name = models.CharField(max_length=150)
#     middle_name = models.CharField(max_length=150, blank=True, null=True)
#     phone_number = models.CharField(max_length=20)
#     birth_date = models.DateField(blank=True, null=True)
#     password = models.CharField(max_length=128)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def __str__(self):
#         return self.email
