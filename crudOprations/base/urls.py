from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('login-user', views.loginPage, name='login-user'),
    path('sign-up', views.signUpPage, name='sign-up'),
    path('logout', views.logoutUser, name='logout'),

]
