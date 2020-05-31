
from django.urls import path
from . import views
import question.views


urlpatterns = [
    path('', views.list, name="list"),
    path('question/new', views.new, name="new"),
    path('question/create', question.views.create, name="create"),
    path('question/<int:question_id>',question.views.detail, name="detail"),
    path('question/edit/<int:question_id>', question.views.edit, name="edit"),
    path('question/update/<int:question_id>', question.views.update, name="update"),
    path('question/delete/<int:question_id>',question.views.delete,name = "delete"),
    # path('question/list', question.views.list, name = "list"),
    #path('question/answer', views.answer, name="answer")
]
