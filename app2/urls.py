from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views

namespace = "app2"
app_name = "app2"

urlpatterns = [
    path(
        "v1/",
        TemplateView.as_view(
            template_name="app2/index.html", extra_context={"data": "I love you"}
        ),
    ),
    path("v2/", views.firstView.as_view()),
    path("v3", RedirectView.as_view(), name="go_to_v3"),
    path("v4/<int:pk>/", views.PostPreLoadTaskView.as_view(), name="redirect-task"),
    path("v5/<int:pk>/", views.SinglePostView.as_view(), name="singlepost"),
]
