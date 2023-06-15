from flask import Flask, request, render_template
from ipl import totalTeams, team1_vs_team2, all_records, batsmanAPI, bowlerAPI


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/all-teams')
def teams():
    teams = totalTeams()
    return teams


@app.route('/teamVSteam')
def getTeamAPI():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = team1_vs_team2(team1, team2)
    return response


@app.route('/team-details')
def team_details():
    team = request.args.get('team')

    response = all_records(team)
    return response


@app.route('/batsman')
def getBatsmanAPI():
    batsman = request.args.get('batsman')
    response = batsmanAPI(batsman)
    return response


@app.route('/bowler')
def getBowlerAPI():
    bowler = request.args.get('bowler')
    response = bowlerAPI(bowler)
    return response


app.run(debug=True)
