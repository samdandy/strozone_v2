from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('roster/<int:team_id>',views.roster,name='roster'),
    path('standings/',views.standings,name='standings'),
    path('team/<int:team_id>',views.team,name='team'),
    path('player/<int:player_id>/<str:group>',views.player,name='player'),
    path('team/<int:team_id>/leaders/pitching',views.team_leaders_pitching,name='team_leaders_pitching'),
    path('team/<int:team_id>/leaders/hitting',views.team_leaders_hitting,name='team_leaders_hitting'),
    path('team/<int:team_id>/roster',views.team_roster,name='team_roster'),
    path('team/<int:team_id>/injured_list',views.team_injured_list,name='team_injured_list')
]
