from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import math

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    prefersDark = models.BooleanField(default='False')
    available = models.BooleanField(default=True)
    gender = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user.username


class ChargeSpot(models.Model):
    name = models.CharField(max_length=50, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    locationText = models.CharField(max_length=20)
    locationUrl = models.URLField()
    typeA = models.IntegerField()
    typeB = models.IntegerField()
    typeC = models.IntegerField()
    wheelchair = models.IntegerField()


class ProcessorPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    belongs = models.ForeignKey(
        ChargeSpot, related_name='processors', on_delete=models.CASCADE)
    available = models.BooleanField()

    def __str__(self):
        return self.belongs.name
