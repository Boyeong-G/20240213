from django.urls import path
from . import views


urlpatterns = [
    path('', views.info_my, name='info'),
    path('login/', views.login_signin, name='login'),
    path('signup/', views.signup_signin, name='signup'),
    path('logout/', views.logout_sign, name='logout'),
]
