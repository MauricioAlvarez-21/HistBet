import HIrecords
import requests
import json
import time
def searchEngine(day):
    leagues=[2014,2021,2002,2019,2015]
    games=list()
    HIrecs=HIrecords.HIrecords
    for league in leagues:
        try:
            url = 'https://api.football-data.org/v4/competitions/'+str(league)+'/matches?matchday='+str(day)
            headers = { 'X-Auth-Token': '87fb1eeae740487aa7587b667ef60da0' }

            response = requests.get(url, headers=headers)

            for match in response.json()['matches']:
                homeTeam_id=match['homeTeam']['id']
                awayTeam_id=match['awayTeam']['id']
                matchID=homeTeam_id*10000+awayTeam_id
                try:
                    if (HIrecs[matchID][1]==True and HIrecs[matchID][0]> 1.2) or (HIrecs[matchID][0]> 2.2):
                        games.append(matchID)
                    if (HIrecs[matchID][1]==True and HIrecs[matchID][0]< -1.2) or (HIrecs[matchID][0]< -2.2):
                        games.append(matchID)
                except:
                    continue
        except:
            continue
    return (games)
