from django.db import models

class User(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return 'id: ' + str(self.id) +  ' email: ' + self.email + ' password: ' + self.password + '<br>'
