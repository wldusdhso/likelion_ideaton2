from django.urls import path
from . import views

app_name='vote'
urlpatterns = [
    path('', views.vote_list, name="vote_list"),
    path('create/', views.create, name='create'),
    path('<int:question_id>/update/', views.update, name='update'),
    path('<int:question_id>/delete/', views.delete, name='delete'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/add_vote/', views.add_vote, name='add_vote'),
]
