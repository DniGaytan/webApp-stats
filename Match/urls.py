from django.urls import path
from Match import views

app_name = 'match'

urlpatterns = [
    path('all/', views.allMatches, name='all'),
    path('create/match', views.createMatch, name='create_match'),
    path('update/<match_id>', views.updateMatch, name='update_match'),
    path('delete/<match_id>', views.deleteMatch, name='delete_match'),
    path('create/tournament', views.createTournament, name='create_tournament'),
    path('update/tournament/<tournament_id>',
         views.updateTournament, name='update_tournament'),
    path('delete/tournament/<tournament_id>',
         views.deleteTournament, name='delete_tournament'),
]
