from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:pk>/', views.question_detail),
    path('<int:pk>/new_comment/', views.new_comment),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('write/', views.question_create, name='question_create'),
    path('edit/<int:pk>/', views.question_edit, name='question_edit'),
    path('delete_<int:pk>/', views.question_delete, name='question_delete'),
]