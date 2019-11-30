from django.urls import path, include
from User import views

app_name = 'user'

urlpatterns = [
    path('login/', views.customLogin, name='login'),
    path('logout/', views.customLogout, name='logout'),
    path('register/', views.customRegister, name='register')
]
