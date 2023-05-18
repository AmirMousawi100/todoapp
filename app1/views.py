from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.http import (HttpResponseBadRequest, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import render

from . import forms, models, util


def home(request): 
    username = request.user
    logged = False
    if request.user.is_authenticated:
       logged = True
       pass
    else:
        return render(request, "app1/home_welcome.html") 

    # todo_list = models.ToDo.objects.all()
    todo_list = list(
        models.ToDo.objects.filter(todo_done=False, todo_username=username)
        .order_by("todo_date")
        .values()
    )
    todo_list_done = list(
        models.ToDo.objects.filter(todo_done=True, todo_username=username).values()
    )
    profile = models.CustomUser.objects.get(user=username)
    return render(
            request,
            "app1/home_activity.html",
            {
                "username"      : username,
                "list"          : todo_list,
                "list_done"     : todo_list_done,
                "profile"       : profile.profile,
                "logged"        : logged
            },
        )
    
        

def home_todo(request):
    username = request.user
    logged = False
    if request.user.is_authenticated:
       logged = True
       pass
    else:
        return render(request, "app1/home_welcome.html") 

    profile = models.CustomUser.objects.get(user=username)
    form = forms.ToDoForm(initial={'todo_username' : f'{username}'})
    if request.method == "POST":
        form = forms.ToDoForm(request.POST, initial={'todo_username' : f'{username}'})
        if form.is_valid():
            print("is valid")
            form.save()
            return HttpResponseRedirect("/app1/my-activity")
        else:
            print("")
            messages.add_message(request, messages.INFO, form.errors)
            return render(request,"app1/home_todo.html",
                {
                    "username"  : username,
                    "error"     : form.errors,
                    "profile"   : profile.profile,
                    "form"      : form,
                    "logged"    : logged
                },
            )
    else:
        return render(
            request,
            "app1/home_todo.html",
            {
                "username"      : username,
                "profile"       : profile.profile,
                "form"          : form,
                "logged"        : logged
            },
        )



def home_test(request):
    return render(request, "app1/home.html")



def AddUserForm2(request):
    form = forms.AddUserDjangoForm()
    if request.method == "POST":
        form = forms.AddUserDjangoForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(True)
            if user:
                profile = models.CustomUser(
                user = user,
                profile = request.FILES['profile']
                )
                profile.save()
                login(request, user)
            return HttpResponseRedirect("/app1")
        else:
            print(form.error_messages)
    else:
        pass
    return render(request, "app1/index.html", {"form": form, "error" : form.errors})


def log_in(request):
    logout(request)
    form = forms.LogInForm()
    if request.method == "POST":
        form = forms.LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # messages.success(request, f"{user.username} logged in.")
                print(f"{user.username} success")
                return HttpResponseRedirect("/app1")
            else:
                messages.error(request, "user with this password does not exist")
                print("user does not exist!!")
                return render(request, "app1/log_in.html", {"form": form})

    return render(request, "app1/log_in.html", {"form": form})


def log_in_success(request):
    username = request.user
    return render(request, "app1/frame.html", {"data": username})


def sign_in_success(request):
    return render(request, "app1/frame.html", {"data": "sign in sucess"})


def test(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if is_ajax:
        if request.method == "GET":
            todos = list(models.Users.objects.all().values())
            return JsonResponse({"context": todos})
        return JsonResponse({"status": "Invalid request"}, status=400)
    else:
        return HttpResponseBadRequest("Invalid request")


def display_todo(request, id):
    todo = models.ToDo.objects.get(id=id)
    form = forms.ToDoForm(instance=todo)
    # to edit the todo object
    if request.method == "POST":
        form = forms.ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            print('saved')
        else:
            print('error below: ')
            messages.add_message(request, messages.INFO, form.errors)
        return render(request, "app1/display_todo.html", {"form": form, "data" : todo})
    else:
        return render(request, "app1/display_todo.html", {"form": form, "data" : todo})


def delete_todo(request, id):
    record = models.ToDo.objects.filter(id=id)
    record_msg = record.delete()
    print(record_msg)
    return HttpResponseRedirect("/app1/my-activity")


def done_todo(request, id):
    record = models.ToDo.objects.get(id=id)
    record.todo_done = True
    record.save()
    return HttpResponseRedirect("/app1/my-activity")


def account(request): 
    #messages.add_message(request, messages.INFO, "ljkhgdf")
    username = request.user  
    profile0 = models.CustomUser.objects.get(user=username)  
    profileForm = forms.CustoUserForm(instance=profile0)
    if request.method == "POST":
        profileForm = forms.CustoUserForm(request.POST, request.FILES, instance=profile0)
        print(profileForm)
        if profileForm.is_valid():
            profileForm.save()
            return HttpResponseRedirect("/app1/account")
    return render(request, "app1/account.html", {
        "username"      : username,
        "profile0"      : profile0.profile, 
        "profileForm"   : profileForm}
        )


def todoid(request):
    todo = models.ToDo.objects.all()
    return render(request, "app1/todoid.html", {"data" : todo})
