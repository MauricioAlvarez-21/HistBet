#import requests
#import json

nameRecs={86: 'Real Madrid CF', 298: 'Girona FC', 81: 'FC Barcelona', 78: 'Club Atlético de Madrid', 77: 'Athletic Club', 264: 'Cádiz CF', 90: 'Real Betis Balompié', 92: 'Real Sociedad de Fútbol', 79: 'CA Osasuna', 263: 'Deportivo Alavés', 95: 'Valencia CF', 87: 'Rayo Vallecano de Madrid', 558: 'RC Celta de Vigo', 82: 'Getafe CF', 94: 'Villarreal CF', 83: 'Granada CF', 89: 'RCD Mallorca', 275: 'UD Las Palmas', 267: 'UD Almería', 559: 'Sevilla FC', 65: 'Manchester City FC', 73: 'Tottenham Hotspur FC', 64: 'Liverpool FC', 563: 'West Ham United FC', 57: 'Arsenal FC', 397: 'Brighton & Hove Albion FC', 354: 'Crystal Palace FC', 402: 'Brentford FC', 351: 'Nottingham Forest FC', 58: 'Aston Villa FC', 66: 'Manchester United FC', 61: 'Chelsea FC', 63: 'Fulham FC', 67: 'Newcastle United FC', 76: 'Wolverhampton Wanderers FC', 1044: 'AFC Bournemouth', 356: 'Sheffield United FC', 62: 'Everton FC', 389: 'Luton Town FC', 328: 'Burnley FC', 3: 'Bayer 04 Leverkusen', 5: 'FC Bayern München', 10: 'VfB Stuttgart', 721: 'RB Leipzig', 28: '1. FC Union Berlin', 2: 'TSG 1899 Hoffenheim', 11: 'VfL Wolfsburg', 17: 'SC Freiburg', 4: 'Borussia Dortmund', 19: 'Eintracht Frankfurt', 12: 'SV Werder Bremen', 16: 'FC Augsburg', 36: 'VfL Bochum 1848', 1: '1. FC Köln', 44: '1. FC Heidenheim 1846', 18: 'Borussia Mönchengladbach', 15: '1. FSV Mainz 05', 55: 'SV Darmstadt 98', 108: 'FC Internazionale Milano', 98: 'AC Milan', 109: 'Juventus FC', 5890: 'US Lecce', 102: 'Atalanta BC', 113: 'SSC Napoli', 450: 'Hellas Verona FC', 99: 'ACF Fiorentina', 103: 'Bologna FC 1909', 470: 'Frosinone Calcio', 586: 'Torino FC', 110: 'SS Lazio', 471: 'US Sassuolo Calcio', 5911: 'AC Monza', 107: 'Genoa CFC', 455: 'US Salernitana 1919', 115: 'Udinese Calcio', 100: 'AS Roma', 104: 'Cagliari Calcio', 445: 'Empoli FC', 548: 'AS Monaco FC', 524: 'Paris Saint-Germain FC', 516: 'Olympique de Marseille', 547: 'Stade de Reims', 521: 'Lille OSC', 512: 'Stade Brestois 29', 529: 'Stade Rennais FC 1901', 522: 'OGC Nice', 576: 'RC Strasbourg Alsace', 533: 'Le Havre AC', 525: 'FC Lorient', 511: 'Toulouse FC', 545: 'FC Metz', 518: 'Montpellier HSC', 543: 'FC Nantes', 541: 'Clermont Foot 63', 546: 'Racing Club de Lens', 523: 'Olympique Lyonnais'}

#leagues=[2014,2021,2002,2019,2015]
#for league in leagues:
#    url = 'https://api.football-data.org/v4/competitions/'+str(league)+'/standings'
#    headers = { 'X-Auth-Token': '87fb1eeae740487aa7587b667ef60da0' }

 #   response = requests.get(url, headers=headers)

  #  count=0
   # for team in response.json()['standings']:
    #    while count < 39:
     #       try:
      #          team_id=team['table'][count]['team']['id']
       #         team_name=team['table'][count]['team']['name']
        #        nameRecs[team_id]=team_name
         #       count+=1
          #  except:
           #     count+=1
            #    continue