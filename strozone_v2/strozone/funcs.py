import statsapi
from .models import *


def lastAnyGameInfo(team_id):
    try:
        lastGameInfoDict = {}
        lastGameID = statsapi.last_game(team_id)
    
        lastGameBox = statsapi.boxscore_data(lastGameID)
        away_team_photo = team_table.objects.get(source_system_id=lastGameBox['teamInfo']['away']['id']).team_img_url
    
        home_team_photo = team_table.objects.get(source_system_id=lastGameBox['teamInfo']['home']['id']).team_img_url

        # print(lastGameBox)
        lastGameInfoDict = {
            'lastGameID':lastGameID,
            'homeTeamID': lastGameBox['teamInfo']['home']['id'],
            'awayTeamID':lastGameBox['teamInfo']['away']['id'],
            'awayTeamName':lastGameBox['teamInfo']['away']['teamName'],
            'homeTeamName':lastGameBox['teamInfo']['home']['teamName'],
            'gameDate': lastGameBox['gameBoxInfo'][-1]['label'],
            'awayTeamRuns':lastGameBox['awayBattingTotals']['r'],
            'homeTeamRuns':lastGameBox['homeBattingTotals']['r'],
            'awayTeamLogo':away_team_photo,
            'homeTeamLogo':home_team_photo
        }

        
        return lastGameInfoDict
    except:
        return None

def nextAnyGameInfo(team_id):
    try:
        nextGameInfoDict = {}
        nextGameID = statsapi.next_game(team_id)
    
        nextGameBox = statsapi.boxscore_data(nextGameID)
        away_team_photo = team_table.objects.get(source_system_id=nextGameBox['teamInfo']['away']['id']).team_img_url
    
        home_team_photo = team_table.objects.get(source_system_id=nextGameBox['teamInfo']['home']['id']).team_img_url

        # print(lastGameBox)
        nextGameInfoDict = {
            'lastGameID':nextGameID,
            'homeTeamID': nextGameBox['teamInfo']['home']['id'],
            'awayTeamID':nextGameBox['teamInfo']['away']['id'],
            'awayTeamName':nextGameBox['teamInfo']['away']['teamName'],
            'homeTeamName':nextGameBox['teamInfo']['home']['teamName'],
            'gameDate': nextGameBox['gameBoxInfo'][-1]['label'],
            'awayTeamRuns':nextGameBox['awayBattingTotals']['r'],
            'homeTeamRuns':nextGameBox['homeBattingTotals']['r'],
            'awayTeamLogo':away_team_photo,
            'homeTeamLogo':home_team_photo
        }

        print(nextGameInfoDict)
        return nextGameInfoDict
    except:
        return None
    
def lastGameInfo():
    try:
        lastGameInfoDict = {}
        lastGameID = statsapi.last_game(117)
    
        lastGameBox = statsapi.boxscore_data(lastGameID)
        away_team_photo = team_table.objects.get(source_system_id=lastGameBox['teamInfo']['away']['id']).team_img_url
    
        home_team_photo = team_table.objects.get(source_system_id=lastGameBox['teamInfo']['home']['id']).team_img_url

        # print(lastGameBox)
        lastGameInfoDict = {
            'lastGameID':lastGameID,
            'homeTeamID': lastGameBox['teamInfo']['home']['id'],
            'awayTeamID':lastGameBox['teamInfo']['away']['id'],
            'awayTeamName':lastGameBox['teamInfo']['away']['teamName'],
            'homeTeamName':lastGameBox['teamInfo']['home']['teamName'],
            'gameDate': lastGameBox['gameBoxInfo'][-1]['label'],
            'awayTeamRuns':lastGameBox['awayBattingTotals']['r'],
            'homeTeamRuns':lastGameBox['homeBattingTotals']['r'],
            'awayTeamLogo':away_team_photo,
            'homeTeamLogo':home_team_photo
        }

        
        return lastGameInfoDict
    except:
        return None

def nextGameInfo():
    try:
        nextGameInfoDict = {}
        nextGameID = statsapi.next_game(117)
    
        nextGameBox = statsapi.boxscore_data(nextGameID)
        away_team_photo = team_table.objects.get(source_system_id=nextGameBox['teamInfo']['away']['id']).team_img_url
    
        home_team_photo = team_table.objects.get(source_system_id=nextGameBox['teamInfo']['home']['id']).team_img_url

        # print(lastGameBox)
        nextGameInfoDict = {
            'lastGameID':nextGameID,
            'homeTeamID': nextGameBox['teamInfo']['home']['id'],
            'awayTeamID':nextGameBox['teamInfo']['away']['id'],
            'awayTeamName':nextGameBox['teamInfo']['away']['teamName'],
            'homeTeamName':nextGameBox['teamInfo']['home']['teamName'],
            'gameDate': nextGameBox['gameBoxInfo'][-1]['label'],
            'awayTeamRuns':nextGameBox['awayBattingTotals']['r'],
            'homeTeamRuns':nextGameBox['homeBattingTotals']['r'],
            'awayTeamLogo':away_team_photo,
            'homeTeamLogo':home_team_photo
        }

        
        return nextGameInfoDict
    except:
        return None

def getTeamLeadersOffensive(team_id,season,season_type,category,limit):
    try:
    
        # for player in data:
        #     print(,,,)
 

       
        players =[]
        # leader_data = statsapi.team_leader_data(team_id, category, season=season, leaderGameTypes=season_type, limit=limit)
        leader_data =statsapi.get('team_leaders',{'season':season,'leaderCategories':category,'teamId':team_id,'limit':limit})['teamLeaders'][0]
        category= leader_data['statGroup']
        leader_data = leader_data['leaders']
        for player in leader_data:
          
            p_rank = player['rank']
            p_name = player['person']['fullName']
            p_value = player['value']
            p_id = player['person']['id']
            player_dict = {
                'rank':p_rank,
                'name':p_name,
                'value':p_value,
                'p_id':p_id,
                'category':category
            }
            players.append(player_dict)
        
        return players
    except:
        return None

# print(lastGameInfo())
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
        return None

def getTeamRoster(team_id):
    try:
        roster1 = statsapi.get(endpoint='team_roster',params={'teamId':team_id})['roster']
        infielders = []
        catchers = []
        pitchers = []
        outfielders = []
        for player in roster1:
            player_data = {
            'player_id':player['person']['id'],
            'player_name':player['person']['fullName'],
            'player_postion_type':player['position']['type'],
            'player_position':player['position']['abbreviation']
            }
            if player['position']['type'] == 'Outfielder':
                player_data['group'] = 'hitting'
                outfielders.append(player_data)
     
            if player['position']['type'] == 'Pitcher':
                player_data['group'] = 'pitching'
                pitchers.append(player_data)
            if player['position']['type'] == 'Catcher':
                player_data['group'] = 'hitting'
                catchers.append(player_data)
            if player['position']['type'] == 'Infielder':
                player_data['group'] = 'hitting'
                infielders.append(player_data)
        player_data ={
            'outfielders':outfielders,
            'pitchers':pitchers,
            'catchers':catchers,
            'infielders':infielders
        }
        return player_data
    except:
        return None


def getPlayerHittingStatsPage(player_id):
    try:
        stat_sections = {}
        stats = statsapi.player_stat_data(personId=player_id,group='hitting',type="career")
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
        stat_sections['header'] = player_header_data
    
        player_career_data ={
            'atBats':stats['stats'][0]['stats']['atBats'],
            'hits': stats['stats'][0]['stats']['hits'],
            'hr': stats['stats'][0]['stats']['homeRuns'],
            'avg': stats['stats'][0]['stats']['avg'],
            'runs': stats['stats'][0]['stats']['runs'],
            'rbi': stats['stats'][0]['stats']['rbi'],
            'rbi': stats['stats'][0]['stats']['rbi'],
            'stolenBases':stats['stats'][0]['stats']['stolenBases'],
            'obp':stats['stats'][0]['stats']['obp'],
            'slg':stats['stats'][0]['stats']['slg'],
            'ops':stats['stats'][0]['stats']['ops'],
            'babip':stats['stats'][0]['stats']['babip']
        }
        stat_sections['career'] = player_career_data

        stats = statsapi.player_stat_data(personId=player_id,group='hitting',type="yearByYear")

        seasons = []
        for i in stats['stats']:
            season ={
            'season':i['season'],
            'atBats':i['stats']['atBats'],
            'hits': i['stats']['hits'],
            'hr': i['stats']['homeRuns'],
            'avg': i['stats']['avg'],
            'runs': i['stats']['runs'],
            'rbi': i['stats']['rbi'],
            'rbi': i['stats']['rbi'],
            'stolenBases':i['stats']['stolenBases'],
            'obp':i['stats']['obp'],
            'slg':i['stats']['slg'],
            'ops':i['stats']['ops'],
            'babip':i['stats']['babip']
            }
            seasons.append(season)
        stat_sections['seasons'] = seasons

        return stat_sections
    except: 
        return None
def getAllStandings(season):
    try:
        fullStandings = {}
        alEastData = []
        alWestData = []
        alCentralData = []
        nlEastData = []
        nlWestData = []
        nlCentralData = []
        standingsData = statsapi.standings_data(leagueId="103,104", division="all", include_wildcard=True, season=season, standingsTypes=None, date=None)
        
        alEastTeams = standingsData[201]['teams']
        for team in alEastTeams:
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['team_id']=team['team_id']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['wc_rank'] = team['wc_rank']
            teamInfo['wc_gb'] = team['wc_gb']
            teamInfo['gamesBack'] = team['gb']
            alEastData.append(teamInfo)
        

        alCentTeams = standingsData[202]['teams']
        for team in alCentTeams:
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['team_id']=team['team_id']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['wc_rank'] = team['wc_rank']
            teamInfo['wc_gb'] = team['wc_gb']
            teamInfo['gamesBack'] = team['gb']
            alCentralData.append(teamInfo)
        

        alWestTeams = standingsData[200]['teams']
        for team in alWestTeams:
         
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['team_id']=team['team_id']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['wc_rank'] = team['wc_rank']
            teamInfo['wc_gb'] = team['wc_gb']
            teamInfo['gamesBack'] = team['gb']
            alWestData.append(teamInfo)
        

        nlEastTeams = standingsData[204]['teams']
        for team in nlEastTeams:
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['team_id']=team['team_id']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['wc_rank'] = team['wc_rank']
            teamInfo['wc_gb'] = team['wc_gb']
            teamInfo['gamesBack'] = team['gb']
            nlEastData.append(teamInfo)
    

        nlCentTeams = standingsData[205]['teams']
        for team in nlCentTeams:
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['team_id']=team['team_id']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['wc_rank'] = team['wc_rank']
            teamInfo['wc_gb'] = team['wc_gb']
            teamInfo['gamesBack'] = team['gb']
            nlCentralData.append(teamInfo)
        

        nlwestTeams = standingsData[203]['teams']
        for team in nlwestTeams:
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['team_id']=team['team_id']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['wc_rank'] = team['wc_rank']
            teamInfo['wc_gb'] = team['wc_gb']
            teamInfo['gamesBack'] = team['gb']
            nlWestData.append(teamInfo)
            
        fullStandings['alWest'] = alWestData
        fullStandings['alEest'] = alEastData
        fullStandings['alCentral'] = alCentralData

        fullStandings['nlWest'] = nlWestData
        fullStandings['nlEest'] = nlEastData
        fullStandings['nlCentral'] = nlCentralData

        return fullStandings
    except:
        return None
def getAlWestStandings(season):
    try:
        alwest_id = division_table.objects.get(name='American League West').source_system_id
        standingsData = statsapi.standings_data(leagueId="103,104", division=alwest_id, include_wildcard=True, season=season, standingsTypes=None, date=None)
        

        alWestData=[]

        alWestTeams = standingsData[200]['teams']
        for team in alWestTeams:
          
            teamInfo = {}
            teamInfo['Name'] = team['name']
            teamInfo['divisonRank'] = team['div_rank']
            teamInfo['wins'] = team['w']
            teamInfo['loss'] = team['l']
            teamInfo['gamesBack'] = team['gb']
            teamInfo['team_id'] = team['team_id']
            alWestData.append(teamInfo)

        return alWestData
    except:
        return None

def getPlayerPitchingStatsPage(player_id):
    try:
        stat_sections = {}
        stats = statsapi.player_stat_data(personId=player_id,group='pitching',type="career")
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
        stat_sections['header'] = player_header_data
        player_career_data ={
            'wins':stats['stats'][0]['stats']['wins'],
            'losses': stats['stats'][0]['stats']['losses'],
            'era': stats['stats'][0]['stats']['era'],
            'gamesPlayed': stats['stats'][0]['stats']['gamesPlayed'],
            'gamesStarted': stats['stats'][0]['stats']['gamesStarted'],
            'saves': stats['stats'][0]['stats']['saves'],
            'inningsPitched': stats['stats'][0]['stats']['inningsPitched'],
            'strikeOuts':stats['stats'][0]['stats']['strikeOuts'],
            'whip':stats['stats'][0]['stats']['whip']
        }
        stat_sections['career'] = player_career_data
        stats = statsapi.player_stat_data(personId=player_id,group='pitching',type="yearByYear")
        seasons = []
        for i in stats['stats']:
            
            season ={
            'season':i['season'],
            'wins':i['stats']['wins'],
            'losses': i['stats']['losses'],
            'gamesPlayed': i['stats']['gamesPlayed'],
            'gamesStarted': i['stats']['gamesStarted'],
            'saves': i['stats']['saves'],
            'inningsPitched': i['stats']['inningsPitched'],
            'whip': i['stats']['whip']
            }
            seasons.append(season)
        stat_sections['seasons'] = seasons
 
        return stat_sections
    except:
        return None

def getTeamLeadersOffensive_final(team_id,season,season_type,category,limit):
    try:
    
        # for player in data:
        #     print(,,,)
 

       
        players =[]
        # leader_data = statsapi.team_leader_data(team_id, category, season=season, leaderGameTypes=season_type, limit=limit)
        leader_data =statsapi.get('team_leaders',{'season':season,'leaderCategories':category,'teamId':team_id,'limit':limit})['teamLeaders']
   
        for leader in leader_data:
         
            if leader['statGroup'] == 'hitting':
  
                cat = leader['statGroup']
                leader_data2 = leader['leaders']
               
        for player in leader_data2:
          
            p_rank = player['rank']
            p_name = player['person']['fullName']
            p_value = player['value']
            p_id = player['person']['id']
            player_dict = {
                'rank':p_rank,
                'name':p_name,
                'value':p_value,
                'p_id':p_id,
                'category':cat
            }
            players.append(player_dict)
        
        return players
    except:
        return None


def getTeamLeadersPitching_final(team_id,season,season_type,category,limit):
    try:
    
        # for player in data:
        #     print(,,,)
 

       
        players =[]
        # leader_data = statsapi.team_leader_data(team_id, category, season=season, leaderGameTypes=season_type, limit=limit)
        leader_data =statsapi.get('team_leaders',{'season':season,'leaderCategories':category,'teamId':team_id,'limit':limit})['teamLeaders']
   
        for leader in leader_data:
         
            if leader['statGroup'] == 'pitching':
  
                cat = leader['statGroup']
                leader_data2 = leader['leaders']
               
        for player in leader_data2:
          
            p_rank = player['rank']
            p_name = player['person']['fullName']
            p_value = player['value']
            p_id = player['person']['id']
            player_dict = {
                'rank':p_rank,
                'name':p_name,
                'value':p_value,
                'p_id':p_id,
                'category':cat
            }
            players.append(player_dict)
        
        return players
    except:
        return None

def getTeamStandings(season,team_id):
    try:
        division_id_pk = team_table.objects.get(source_system_id=team_id).division_id
        division_id_src = division_table.objects.get(division_id = division_id_pk).source_system_id
        standingsData = statsapi.standings_data(leagueId="103,104", division=division_id_src, include_wildcard=True, season=season, standingsTypes=None, date=None)
        
        divisionData=[]

        teams_records = standingsData[int(division_id_src)]['teams']
        for team in teams_records:
          
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


# def getPlayerHittingStatsPage(player_id):
#     try:
#         stat_sections = {}
#         stats = statsapi.player_stat_data(personId=player_id,group='hitting',type="career")


# nextGameBox = statsapi.boxscore_data(nextGameID)
# nextGameInfoDict['nextGameID'] = nextGameID




# print(statsapi.get(endpoint='teams',params={}))

# print(statsapi.get(endpoint='teams',params={}))

# print(statsapi.get(endpoint='sports',params={'sportId':1}))

sport_id = 1
al_league = 103
nl_league = 104

# leagues = statsapi.get(endpoint='league',params={'sportId':sport_id})['leagues']
# print(leagues)

# for l in leagues:
#     print(l['id'],l['name'])

# divisions = statsapi.get(endpoint='divisions',params={'sportId':sport_id})['divisions']
# print(divisions)

# for d in divisions:
#     print(d['id'],d['name'],d['league']['id'])

# nl_teams = statsapi.get(endpoint='teams',params={'sportId':sport_id,'leagueIds':nl_league})['teams']
# # print(nl_teams)
# for team in nl_teams:
#     print("("+"'"+str(team['division']['id'])+"',"+
#         str("'"+team['name']+"',"),"'"+team['locationName']+"',","''",",'"+str(team['id'])+"'"+", current_timestamp),"
        
#         )
# al_teams = statsapi.get(endpoint='teams',params={'sportId':sport_id,'leagueIds':al_league})['teams']

# for team in al_teams:
#     print("("+"'"+str(team['division']['id'])+"',"+
#         str("'"+team['name']+"',"),"'"+team['locationName']+"',","''",",'"+str(team['id'])+"'"+", current_timestamp),"
        
#         )

# 

# for team in al_teams:
#     print("("+
#         str("'"+team['name']+"',"),"'"+team['locationName']+"',","''",",'"+str(team['id'])+"'"+", current_timestamp)")
