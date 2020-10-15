from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    nickname = models.CharField(max_length=40, default='')
    prefersDark = models.BooleanField(default='False')
    available = models.BooleanField(default=True)
    gender = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user.username
