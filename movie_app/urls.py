from django.urls import path
from . import views
from .views import movie_list, movie_list2, movie_list3, movie_list4, movie_list5


urlpatterns = [

    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name="user-logout"),
    path('movie_list/', movie_list, name='movie_list'),
    path('movie_list2/', movie_list2, name='movie_list2'),
    path('movie_list3/', movie_list3, name='movie_list3'),
    path('movie_list4/', movie_list4, name='movie_list4'),
    path('movie_list5/', movie_list5, name='movie_list5'),
    path('about/', views.about, name='about'),

]