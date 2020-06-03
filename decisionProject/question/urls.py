
from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:question_id>', views.detail, name="detail"),
    path('edit/<int:question_id>', views.edit, name="edit"),
    path('update/<int:question_id>', views.update, name="update"),
    path('delete/<int:question_id>', views.delete,name = "delete"),
    path('create_answer/<int:question_id>', views.create_answer,name="create_answer"),
    path('update_answer/<int:answer_id>', views.update_answer,name="update_answer"),
    path('edit_answer/<int:answer_id>', views.edit_answer,name="edit_answer"),
    #path('answer/<int:answer_id>', views.answer,name="answer"),
]
