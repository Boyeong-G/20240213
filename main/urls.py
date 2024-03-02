from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_list, name='home'),
    path('my/', views.my_list, name='my_list'),
    path('my/question/', views.my_list_question, name='my_list_question'),
    path('my/likes/', views.my_list_likes, name='my_list_likes'),
]