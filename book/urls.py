from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add/", views.AddBookView.as_view(), name="add"),
    path("c/<str:genre>", views.CategoryListView.as_view(), name="list-view"),
    path("<slug:slug>/edit", views.UpdateBookView.as_view(), name="book-detail"),
    path("display/<slug:slug>/", views.BookDetailView.as_view(), name="book-detail"),
]
