from flask import Flask, render_template, flash, get_flashed_messages, redirect, url_for, request
import datetime
import searchEngine
import nameRecs
import dataRetrieved
import HIrecords


app=Flask(__name__)
app.config['SECRET_KEY']='MauricioRafael2103'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        matchDay = request.form['matchDay']
        info=[]
        games=searchEngine.searchEngine(matchDay)
        for game in games:
            teamA=(game//10000)
            teamA_name=nameRecs.nameRecs[teamA]
            teamB=game-(teamA*10000)
            teamB_name=nameRecs.nameRecs[teamB]
            pastResults=dataRetrieved.dataRetrieved[game]
            historicAverage=str(HIrecords.HIrecords[game][0])
            if HIrecords.HIrecords[game][0]>0:
                winner=teamA_name
            elif HIrecords.HIrecords[game][0]<0:
                winner=teamB_name
            if HIrecords.HIrecords[game][1]==True:
                standardStatus="Results are historically standard"
            elif HIrecords.HIrecords[game][1]==False: 
                standardStatus="Results are not standard"
            data=[teamA_name,teamB_name, winner, pastResults,historicAverage[:5], standardStatus, matchDay]
            info.append(data)
        return render_template('index.html', info=info)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
