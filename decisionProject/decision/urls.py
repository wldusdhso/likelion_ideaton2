from django.contrib import admin
from django.urls import path
from . import views
import decision.views

urlpatterns = [
    path('', views.list, name="list"),
    path('result', views.result, name = "result"),
]
