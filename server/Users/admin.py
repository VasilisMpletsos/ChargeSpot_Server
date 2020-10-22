from django.contrib import admin
from .models import UserProfile, ChargeSpot, ChargeHistory, ProcessorPoint, Management

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ChargeSpot)
admin.site.register(ChargeHistory)
admin.site.register(ProcessorPoint)
admin.site.register(Management)
