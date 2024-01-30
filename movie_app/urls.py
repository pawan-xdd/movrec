from django.urls import path
from . import views
from .views import movie_list


urlpatterns = [

    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name="user-logout"),
    path('movie_list/', movie_list, name='movie_list'),

]