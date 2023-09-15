import HIrecords
import requests
import json
import time

matchDays=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
leagues=[2014,2021,2002,2019,2015]
HIrecs=HIrecords.HIrecords

for day in matchDays:
    dataAnalyzed=0
    success=0

    for league in leagues:
        url = 'https://api.football-data.org/v4/competitions/'+str(league)+'/matches?matchday='+str(day)+'&season=2022'
        headers = { 'X-Auth-Token': '87fb1eeae740487aa7587b667ef60da0' }

        response = requests.get(url, headers=headers)

        for match in response.json()['matches']:
            homeTeam_id=match['homeTeam']['id']
            awayTeam_id=match['awayTeam']['id']
            matchID=homeTeam_id*10000+awayTeam_id
            try:
                if (HIrecs[matchID][1]==True and HIrecs[matchID][0]> 1.2) or (HIrecs[matchID][0]> 2.2):
                    if match['score']['winner']=='HOME_TEAM':
                        dataAnalyzed+=1
                        success+=1
                    else:
                        dataAnalyzed+=1
                if (HIrecs[matchID][1]==True and HIrecs[matchID][0]< -1.2) or (HIrecs[matchID][0]< -2.2):
                    if match['score']['winner']=='AWAY_TEAM':
                        dataAnalyzed+=1
                        success+=1
                    else:
                        dataAnalyzed+=1
            except:
                continue
    if (dataAnalyzed)==0:
        print("Day " + str(day))
        print("No safe bets today")
        print("\n")
        time.sleep(40)
    else:
        print("Day " + str(day))
        successRate=(success/dataAnalyzed)*100
        print (successRate)
        print(dataAnalyzed)
        print("\n")
        time.sleep(40)