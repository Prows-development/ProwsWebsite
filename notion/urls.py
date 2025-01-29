from django.contrib import admin
from django.urls import path
from . import views

app_name = "notion"


urlpatterns = [
    path("notion/", views.notion, name="index"),
]