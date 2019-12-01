from django.urls import path
from Match import views

app_name = 'match'

urlpatterns = [
    path('all/', views.allMatches, name='create'),
    path('update/<match_id>', views.updateMatch, name='update'),
    path('delete/<match_id>', views.deleteMatch, name='delete')
]
