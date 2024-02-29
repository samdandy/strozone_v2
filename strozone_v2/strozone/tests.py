from django.test import TestCase
import statsapi


# Create your tests here.

nextGameInfoDict = {}
nextGameID = statsapi.next_game(117)


url = 'https://statsapi.mlb.com/api/v1/stats/leaders'

def getAstrosLeaders(season,season_type,category,limit):
    try:
        players =[]
        leader_data = statsapi.team_leader_data('117', category, season=season, leaderGameTypes=season_type, limit=limit)
        
        for player in leader_data:
            p_rank = player[0]
            p_name = player[1]
            p_value = player[2]
            player_dict = {
                'rank':p_rank,
                'name':p_name,
                'value':p_value
            }
            players.append(player_dict)
        
        return players
    except:
        print('failed to grab data')



def getTeamRoster(team_id):
    try:
        roster1 = statsapi.get(endpoint='team_roster',params={'teamId':team_id})['roster']
        players = []
        for player in roster1:
            player_data = {
            'player_id':player['person']['id'],
            'player_name':player['person']['fullName'],
            'player_postion_type':player['position']['type'],
            'player_position':player['position']['abbreviation']
            }
            players.append(player_data)
    except:
        return None

def getPlayerHittingStats(player_id,type):
    try:

        stats = statsapi.player_stat_data(personId=player_id,group='hitting',type=type)
        player_header_data ={
            'player_id':stats['id'],
            'first_name':stats['first_name'],
            'last_name':stats['last_name'],
            'full_name': stats['first_name'] + ' ' + stats['last_name'],
            'current_team':stats['current_team'],
            'position':stats['position'],
            'batting_side':stats['bat_side'],
            'throwing_hand':stats['pitch_hand']
        }
        print(player_header_data)
        return player_header_data
    except: 
        return None
def getStandings(season,team_id):
    try:
        division_id_pk = division_table.objects.get(name='American League West').source_system_id
        standingsData = statsapi.standings_data(leagueId="103,104", division=division_id, include_wildcard=True, season=season, standingsTypes=None, date=None)
        

        divisionData=[]

        teams_records = standingsData[200]['teams']
        for team in teams_records:
            print(team)
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['gamesBack'] = team['gb']
            teamInfo['team_id'] = team['team_id']
            divisionData.append(teamInfo)

        return divisionData
    except:
        return None


standingsData = statsapi.standings_data(leagueId="103,104", division=2, include_wildcard=True, season=2023, standingsTypes=None, date=None)
print(standingsData)
# print((stats['stats'][0]['stats']['gamesPlayed'],stats['stats'][0]['stats']['runs'],stats['stats'][0]['stats']['doubles'],stats['stats'][0]['stats']['triples'],stats['stats'][0]['stats']['homeRuns'],stats['stats'][0]['stats']['strikeOuts'],stats['stats'][0]['stats']['baseOnBalls'],stats['stats'][0]['stats']['hits'],stats['stats'][0]['stats']['hitByPitch'],stats['stats'][0]['stats']['avg'],stats['stats'][0]['stats']['atBats'],stats['stats'][0]['stats']['obp'],stats['stats'][0]['stats']['slg'],stats['stats'][0]['stats']['ops'],stats['stats'][0]['stats']['stolenBases']))
# for s in stats:
#     print(s)


#

# standingsData = statsapi.standings_data(leagueId="103,104", division=200, include_wildcard=True, season=2023, standingsTypes=None, date=None)
# meta('statGroups') to look up valid values for group, and meta('statTypes')

# statTypes = statsapi.get('meta',{'type':'statGroups'})
# print(statTypes)

# baseballStats = statsapi.get('meta',{'type':'leagueLeaderTypes'})
# # print(baseballStats)

# for stat in baseballStats:
#     name = stat['displayName']
#     print("('"+name+"'),")
# # #     groups = stat['statGroups']
# # #     for group in groups:

        
# # #         print("('"+name+"'"+','+"'"+name+"'"+','+"'"+group['displayName']+"',current_timestamp),")
            

# data = statsapi.get('stats_leaders',{'season':,'leaderCategories':'battingAverage','statGroup':'hitting','teamId':117})    


# 1: HITTING 
# 2: pitching
# 3: CATCHING 
# print('test')

# data = stat_type_table.objects.values('display_name', 'lookup_name')
# print(data)
# print(leader_data[-1])
# for l in data:
#     print(l)

# [0]['leaders']
# for player in data:
#     print(player['rank'],player['value'],player['person']['fullName'],player['person']['id'])


# alWestData=[]

# alWestTeams = standingsData[200]['teams']
# for team in alWestTeams:
#     print(team)
#     teamInfo = {}
#     teamInfo['Name'] = team['name']
#     teamInfo['divisonRank'] = team['div_rank']
#     teamInfo['wins'] = team['w']
#     teamInfo['loss'] = team['l']
#     teamInfo['gamesBack'] = team['gb']
#     teamInfo['team_id'] = team['team_id']
#     alWestData.append(teamInfo)
# for player in leader_data:

#     p_rank = player['rank']
#     p_name = player['person']['fullName']
#     p_value = player['value']
#     p_id = player['person']['id']
#     player_dict = {
#         'rank':p_rank,
#         'name':p_name,
#         'value':p_value,
#         'p_id':p_id
#     }
#     players.append(player_dict)
# print(players)

# Use meta('statGroups')

# [{'displayName': 'hitting'}, {'displayName': 'pitching'}, {'displayName': 'fielding'}, 
# {'displayName': 'catching'}, {'displayName': 'running'}, {'displayName': 'game'}, {'displayName': 'team'}, {'displayName': 'streak'}]