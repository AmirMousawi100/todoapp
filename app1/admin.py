from django.contrib import admin
from app1.models import CustomUser, Nurse, ToDo

# Register your models here.



admin.site.register(CustomUser)
admin.site.register(Nurse)
admin.site.register(ToDo)