from django.db import models


class User(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"


