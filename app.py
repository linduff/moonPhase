from flask import Flask, render_template, redirect, jsonify
from datetime import datetime
from astral import moon

app = Flask(__name__)

@app.route("/")
def whatPhaseIsTheMoon():
    current_date = datetime.now()
    phaseNumber = moon.phase(current_date)
    phaseName = getPhaseName(phaseNumber)
    return render_template("moonPhase.html", phaseNumber = "{:.3f}".format(phaseNumber), phaseName = phaseName)

@app.route('/healthcheck')
def health():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

def getPhaseName(phaseNumber):
    if phaseNumber < 0.5 or phaseNumber > 27.5:
        return "New Moon"
    elif phaseNumber >= 0.5 and phaseNumber <= 6.5:
        return "Waxing Crescant"
    elif phaseNumber > 6.5 and phaseNumber < 7.5:
        return "First Quarter"
    elif phaseNumber >= 7.5 and phaseNumber <= 13.5:
        return "Waxing Gibbous"
    elif phaseNumber > 13.5 and phaseNumber < 14.5:
        return "Full Moon"
    elif phaseNumber >= 14.5 and phaseNumber <= 20.5:
        return "Waning Gibbous"
    elif phaseNumber > 20.5 and phaseNumber < 21.5:
        return "Third Quarter"
    else:
        return "Waning Crescant"
    

if __name__ == "__main__":
    app.run()