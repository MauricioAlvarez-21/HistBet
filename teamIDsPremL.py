import requests
import json

url = 'https://api.football-data.org/v4/competitions/2021/standings'
headers = { 'X-Auth-Token': '87fb1eeae740487aa7587b667ef60da0' }

response = requests.get(url, headers=headers)

#count=0
for team in response.json()['standings']:
    print ("\n\n")
    team_id=team['table'][0]['team']['id']
    team_name=team['table'][0]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][1]['team']['id']
    team_name=team['table'][1]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][2]['team']['id']
    team_name=team['table'][2]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][3]['team']['id']
    team_name=team['table'][3]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][4]['team']['id']
    team_name=team['table'][4]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][5]['team']['id']
    team_name=team['table'][5]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][6]['team']['id']
    team_name=team['table'][6]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][7]['team']['id']
    team_name=team['table'][7]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][8]['team']['id']
    team_name=team['table'][8]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][9]['team']['id']
    team_name=team['table'][9]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][10]['team']['id']
    team_name=team['table'][10]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][11]['team']['id']
    team_name=team['table'][11]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][12]['team']['id']
    team_name=team['table'][12]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][13]['team']['id']
    team_name=team['table'][13]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][14]['team']['id']
    team_name=team['table'][14]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][15]['team']['id']
    team_name=team['table'][15]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][16]['team']['id']
    team_name=team['table'][16]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][17]['team']['id']
    team_name=team['table'][17]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][18]['team']['id']
    team_name=team['table'][18]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    team_id=team['table'][19]['team']['id']
    team_name=team['table'][19]['team']['name']
    print("Team: ", team_name, "   ID:", team_id)
    print ("\n\n")
    