
from django.urls import path
from . import views
import question.views







urlpatterns = [
    path('', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('create/', question.views.create, name="create"),
    path('<int:question_id>', question.views.detail, name="detail"),
    path('edit/<int:question_id>', question.views.edit, name="edit"),
    path('update/<int:question_id>', question.views.update, name="update"),
    path('delete/<int:question_id>', question.views.delete,name = "delete"),
    path('create_answer/<int:question_id>', views.create_answer,name="create_answer"),
    path('update_answer/<int:answer_id>', question.views.update_answer,name="update_answer"),
    path('edit_answer/<int:answer_id>', question.views.edit_answer,name="edit_answer"),
    #path('answer/<int:answer_id>', question.views.answer,name="answer"),
]
