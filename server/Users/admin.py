from django.contrib import admin
from .models import UserProfile, ChargeSpot, ProcessorPoint

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ChargeSpot)
admin.site.register(ProcessorPoint)
