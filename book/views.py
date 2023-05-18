from django.shortcuts import render
from book.models import Books
from django.views.generic import (
    TemplateView,
    DetailView,
    RedirectView,
    ListView,
    FormView,
    CreateView,
    UpdateView,
)
from django.db.models import F
from django.utils import timezone
from .forms import AddForm

# Create your views here.


class IndexView(ListView):
    model = Books
    template_name = "book/index.html"
    context_object_name = "books"
    paginate_by = 1


class CategoryListView(ListView):
    model = Books
    template_name = "book/index.html"
    context_object_name = "books"
    paginate_by = 1

    def get_queryset(self):
        return Books.objects.filter(genre__icontains=self.kwargs.get("genre"))


class AddBookView(CreateView):
    template_name = "book/add.html"
    form_class = AddForm
    success_url = "/book/"


class UpdateBookView(UpdateView):
    model = Books
    template_name = "book/add.html"
    form_class = AddForm
    success_url = "/book/"


class RedirectToCounter(RedirectView):
    url = ""

    def get_redirect_url(self, *args, **kwargs):
        book = Books.objects.filter(slug=self.kwargs.get("slug"))
        book.update(count=F("count") + 1)
        return super().get_redirect_url(*args, **kwargs)


class BookDetailView(DetailView):
    model = Books
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Books.objects.filter(slug=self.kwargs.get("slug"))
        book.update(count=F("count") + 1)

        context["time"] = timezone.now()
        return context
