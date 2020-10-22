from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import math
from decimal import Decimal

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    prefersDark = models.BooleanField(default='False')
    available = models.BooleanField(default=True)
    gender = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=20, default='')
    account = models.DecimalField(
        max_digits=4, decimal_places=2, default=Decimal('00.00'))

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


class ChargeHistory(models.Model):
    userHistory = models.ForeignKey(
        User, related_name='history', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    money = models.DecimalField(
        max_digits=4, decimal_places=2, default=Decimal('00.00'))
    duration = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        unique_together = ['userHistory', 'date', 'duration']
        ordering = ['date']

    def __str__(self):
        return self.userHistory.username


class ProcessorPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    belongs = models.ForeignKey(
        ChargeSpot, related_name='processors', on_delete=models.CASCADE)
    available = models.BooleanField()

    def __str__(self):
        return self.belongs.name


class Management(models.Model):
    belongs = models.OneToOneField(ChargeSpot, on_delete=models.CASCADE)
    batteryVolt = models.DecimalField(max_digits=4, decimal_places=2)
    fullVolt = models.DecimalField(max_digits=4, decimal_places=2)
    panels = models.IntegerField()
    panelsVolt = models.DecimalField(max_digits=4, decimal_places=2)
    panelsFullVolt = models.DecimalField(max_digits=4, decimal_places=2)
