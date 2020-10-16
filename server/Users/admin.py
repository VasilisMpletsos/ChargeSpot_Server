from django.contrib import admin
from .models import UserProfile, ChargeSpot, ProcessorPoint, Management

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ChargeSpot)
admin.site.register(ProcessorPoint)
admin.site.register(Management)
