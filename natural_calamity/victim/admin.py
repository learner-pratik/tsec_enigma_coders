from django.contrib import admin
from .models import adminDB, Login
from .models import Volunteer
admin.site.register(adminDB)
admin.site.register(Volunteer)
admin.site.register(Login)
# Register your models here.
