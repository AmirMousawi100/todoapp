from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.


class CustomUser(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.FileField(upload_to="static/media/profile/")

class Nurse(models.Model):
    title = models.CharField(max_length=300) 


def check_todo_date(value):
    list = str(value).split("-")
    list_current = str(timezone.localdate()).split("-")
    if int(list[0]) < int(list_current[0]):
        raise ValidationError("""This date(year) is before current date. 
                              Please submit an appropriate date.""")
    elif int(list[1]) < int(list_current[1]):
        raise ValidationError("""This date(month) is before current date. 
                              Please submit an appropriate date.""")
    elif int(list[2]) < int(list_current[2]):
        raise ValidationError("""This date(day) is before current date. 
                              Please submit an appropriate date.""")
    


class ToDo(models.Model):
    todo_title      = models.CharField(max_length=300) 
    todo_content    = models.CharField(max_length=1000)
    todo_date       = models.DateField(null=True, validators=[check_todo_date])
    todo_time       = models.TimeField(null=True)
    todo_username   = models.CharField(max_length=100)
    todo_done       = models.BooleanField(default=False)
    count           = models.IntegerField(default=0)  

    def clean(self):
        t = timezone.localtime()
        print(t)
        user_date = str(self.todo_date)
        user_time = str(self.todo_time)
        user_time_list = str(user_time).split(":")
        print(user_date)
        print(user_time)
        current = str(timezone.localtime()).split(" ")
        current_date = current[0]
        current_time = current[1].split(":")

        # check today
        if (user_date == current_date):
            print("equal")
            if user_time_list[0] < current_time[0]:
                raise ValidationError("hour is old")
            elif (user_time_list[0] == current_time[0] and user_time_list[1] < current_time[1]):
                raise ValidationError("minutes old")    




        

