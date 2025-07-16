from django.contrib import admin

# Register your models here.
#accounts/admin.py
from .models import *

admin.site.register(HotelUser)
admin.site.register(HotelVendor)

admin.site.register(Ameneties)