from django.urls import path
from Hub import views

app_name = 'hub'

urlpatterns = [
    path('home/', views.getHome, name='home')
]
