from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from app1 import models
from book.models import Books
from django.db.models import F

# Create your views here.


class firstView(TemplateView):
    template_name = "app2/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = models.ToDo.objects.all()
        return context


class PostPreLoadTaskView(RedirectView):
    # url = "http://www.google.com"
    pattern_name = "app2:singlepost"

    def get_redirect_url(self, *args, **kwargs):
        post = models.ToDo.objects.filter(todo_id=kwargs["pk"])
        post.update(count=F("count") + 1)
        return super().get_redirect_url(*args, **kwargs)


class SinglePostView(TemplateView):
    template_name = "app2/index2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = get_object_or_404(models.ToDo, todo_id=self.kwargs.get("pk"))
        print(result)
        context["posts"] = result
        return context
