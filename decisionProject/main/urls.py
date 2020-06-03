from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name="home"),
    path('mypage/<str:profile_name>', views.mypage, name="mypage"),
    path('register/',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]

