from django.contrib import admin
from .models import adminDB
from .models import Volunteer
admin.site.register(adminDB)
admin.site.register(Volunteer)
# Register your models here.
