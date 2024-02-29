from django.shortcuts import render
from django.http import HttpResponse
from .funcs import *
from .forms import *
import json
SEASON = 2023


def home(request):

    

    standings_data = getAlWestStandings(season=SEASON)
 
    last_game_data = lastGameInfo()
    next_game_data = nextGameInfo()

    ops_leaders =getTeamLeadersOffensive(117,season=SEASON,season_type="R",category="ops",limit=5)
    hr_leaders = getTeamLeadersOffensive(117,season=SEASON,season_type='R',category='homeruns',limit=5)
    era_leaders = getTeamLeadersOffensive(117,season=SEASON,season_type='R',category='earnedRunAverage',limit=5)
    whip_leaders = getTeamLeadersOffensive(117,season=SEASON,season_type='R',category='walksAndHitsPerInningPitched',limit=5)

    # ops_leaders = getAstrosLeaders(season=SEASON,season_type='R',category='onBasePlusSlugging',limit=5)
    # hr_leaders = getAstrosLeaders(season=SEASON,season_type='R',category='homeruns',limit=5)
    # era_leaders = getAstrosLeaders(season=SEASON,season_type='R',category='earnedRunAverage',limit=5)
    # whip_leaders = getAstrosLeaders(season=SEASON,season_type='R',category='walksAndHitsPerInningPitched',limit=5)
    return render(request, 'home.html',{'lastGameInfo':last_game_data, 'ops_leaders':ops_leaders,'hr_leaders':hr_leaders,'era_leaders':era_leaders,'nextGameInfo':next_game_data,'standings':standings_data})


def roster(request,team_id):
    roster_data = getTeamRoster(team_id=team_id)
    outfielders = roster_data['outfielders']
    infielders = roster_data['infielders']
    pitchers = roster_data['pitchers']
    catchers = roster_data['catchers']
    return render(request, 'roster.html',{'catchers':catchers,'pitchers':pitchers,'infielders':infielders,'outfielders':outfielders})

def standings(request):
    standings_data = getAllStandings(season=SEASON)
    al_west = standings_data['alWest']
    al_east = standings_data['alEest']
    al_central = standings_data['alCentral']

    nl_west = standings_data['nlWest']
    nl_east = standings_data['nlEest']
    nl_central = standings_data['nlCentral']

    return render(request, 'standings.html',{'al_west':al_west,'al_east':al_east,'al_central':al_central,'nl_west':nl_west,'nl_east':nl_east,'nl_central':nl_central})

def team(request,team_id):
    team_standings = getTeamStandings(season=SEASON,team_id=team_id)
    last_game_data = lastAnyGameInfo(team_id=team_id)
    next_game_data = nextAnyGameInfo(team_id=team_id)
    ops_leaders =getTeamLeadersOffensive(team_id,season=SEASON,season_type="R",category="ops",limit=5)
    hr_leaders = getTeamLeadersOffensive(team_id,season=SEASON,season_type='R',category='homeruns',limit=5)
    era_leaders = getTeamLeadersOffensive(team_id,season=SEASON,season_type='R',category='earnedRunAverage',limit=5)
    whip_leaders = getTeamLeadersOffensive(team_id,season=SEASON,season_type='R',category='walksAndHitsPerInningPitched',limit=5)
    
    

 
    # return render(request, 'team.html',{'lastGameInfo':last_game_data,'nextGameInfo':next_game_data, 'ops_leaders':ops_leaders,'hr_leaders':hr_leaders,'era_leaders':era_leaders,'whip_leaders':whip_leaders})
    return render(request, 'team.html',{'lastGameInfo':last_game_data,'nextGameInfo':next_game_data, 'ops_leaders':ops_leaders,'hr_leaders':hr_leaders,'era_leaders':era_leaders,'whip_leaders':whip_leaders,'leader_lookup_form_hitting':None,'leader_lookup_form_pitching':None,'team_id':team_id,'standings':team_standings})

def player(request,player_id,group):
    print(group)
    if group == 'hitting':
        data = getPlayerHittingStatsPage(player_id=player_id)
        header = data['header']
        career = data['career']
        seasons = data['seasons']
        p_type = 'hitter'
    else:
        data = getPlayerPitchingStatsPage(player_id=player_id)
        header = data['header']
        career = data['career']
        seasons = data['seasons']
        p_type = 'pitcher'
    return render(request, 'player.html',{'header':header,'career':career,'seasons':seasons,'p_type':p_type})



def team_leaders_hitting(request,team_id):
    if request.method == 'POST':
        leader_lookup_form = Leader_lookup_hitting(request.POST)
        if leader_lookup_form.is_valid():
            print(leader_lookup_form.cleaned_data['stat'])
            leaders = getTeamLeadersOffensive_final(season=SEASON,season_type="R",category=leader_lookup_form.cleaned_data['stat'],limit=10,team_id=team_id)
        return render(request, 'team_leaders_hitting.html',{'team_id':team_id,'leader_lookup_form':leader_lookup_form,'leaders':leaders})
    else:
        leader_lookup_form = Leader_lookup_hitting(request.POST or None)
 

        return render(request, 'team_leaders_hitting.html',{'team_id':team_id,'leader_lookup_form':leader_lookup_form,'leaders':None})

def team_leaders_pitching(request,team_id):
    if request.method == 'POST':
        leader_lookup_form = Leader_lookup_pitching(request.POST)
        if leader_lookup_form.is_valid():
            print(leader_lookup_form.cleaned_data['stat'])
            leaders = getTeamLeadersPitching_final(season=SEASON,season_type="R",category=leader_lookup_form.cleaned_data['stat'],limit=10,team_id=team_id)
        return render(request, 'team_leaders_pitching.html',{'team_id':team_id,'leader_lookup_form':leader_lookup_form,'leaders':leaders})
    else:
        leader_lookup_form = Leader_lookup_pitching(request.POST or None)
 

        return render(request, 'team_leaders_pitching.html',{'team_id':team_id,'leader_lookup_form':leader_lookup_form,'leaders':None})

def team_roster(request,team_id):
    roster_data = getTeamRoster(team_id=team_id)
    outfielders = roster_data['outfielders']
    infielders = roster_data['infielders']
    pitchers = roster_data['pitchers']
    catchers = roster_data['catchers']

    return render(request, 'team_roster.html',{'team_id':team_id,'catchers':catchers,'pitchers':pitchers,'infielders':infielders,'outfielders':outfielders})

def team_injured_list(request,team_id):
    return render(request, 'team_injured_list.html',{'team_id':team_id})