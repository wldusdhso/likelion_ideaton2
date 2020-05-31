
from django.urls import path
from . import views
import question.views


urlpatterns = [
    path('', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('create/', question.views.create, name="create"),
    path('<int:question_id>',question.views.detail, name="detail"),
    path('edit/<int:question_id>', question.views.edit, name="edit"),
    path('update/<int:question_id>', question.views.update, name="update"),
    path('delete/<int:question_id>',question.views.delete,name = "delete"),
    # path('list', question.views.list, name = "list"),
    path('create_answer/<int:question_id>', views.create_answer,name="create_answer"),
    path('answer_edit/<int:question_id>',views.answer_edit,name="answer_edit"),
]
