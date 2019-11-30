from django.urls import path
from Hub import views


urlpatterns = [
    path('home/', views.getHome, name='home')
]
