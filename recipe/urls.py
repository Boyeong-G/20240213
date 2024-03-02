from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('hot_recipes/', views.recipe_list_hot, name='recipe_list_hot'),
    path('recent_recipes/', views.recipe_list_recent, name='recipe_list_recent'),
    path('<int:pk>/', views.recipe_detail),
    path('<int:pk>/likes/', views.likes, name='likes'),
    path('write/', views.recipe_create, name='recipe_create'),
    path('edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('delete_<int:pk>/', views.recipe_delete, name='recipe_delete'),
]