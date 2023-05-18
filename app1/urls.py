from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("compose-todo", views.home_todo),
    path("my-activity", views.home),
    path("my-activity/display/<int:id>", views.display_todo),
    path("compose-todo", views.home),
    path("home", views.home_test),
    path("sign_in", views.AddUserForm2),
    path("sign_in_success", views.sign_in_success),
    path("log_in", views.log_in),
    path("log_in_success", views.log_in_success),
    path("testdata", views.test),
    path("delete/<int:id>", views.delete_todo),
    path("done/<int:id>", views.done_todo),
    path("account", views.account),
    path("todo_id", views.todoid),
    path("myapp", views.home_todo)
]
