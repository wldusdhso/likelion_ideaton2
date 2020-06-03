from django.contrib import admin
from django.urls import path
from . import views

app_name='decision'

urlpatterns = [
    path('', views.list, name="list"),
    path('result', views.result, name = "result"),
    path('delete/<int:decision_id>', views.delete, name = "delete"),
]
