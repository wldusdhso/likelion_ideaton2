from django.contrib import admin
from django.urls import path
from . import views
import decision.views

app_name='decision'

urlpatterns = [
    path('', views.list, name="list"),
    path('result', views.result, name = "result"),
]
