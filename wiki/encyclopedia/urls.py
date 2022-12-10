from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", RedirectView.as_view(permanent=False, url='wiki')),
    path("wiki", views.index, name="index"),
    path("wiki/<str:name>", views.entry, name = "entry"),
    path("search", views.search, name = "search"),
    path("create", views.create, name = "create"),
    path("edit", views.index, name = "index"),
    path("edit/<str:name>", views.edit, name = "edit"),
    path("random", views.random, name = "random"),
]
