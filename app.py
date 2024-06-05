from flask import Flask, render_template, redirect
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
    if phaseNumber < 1 or phaseNumber > 27:
        return "New Moon"
    elif phaseNumber >= 1 and phaseNumber <= 6:
        return "Waxing Crescant"
    elif phaseNumber > 6 and phaseNumber < 8:
        return "First Quarter"
    elif phaseNumber >= 8 and phaseNumber <= 13:
        return "Waxing Gibbous"
    elif phaseNumber > 13 and phaseNumber < 15:
        return "Full Moon"
    elif phaseNumber >= 15 and phaseNumber <= 20:
        return "Waning Gibbous"
    elif phaseNumber > 20 and phaseNumber < 22:
        return "Third Quarter"
    else:
        return "Waning Crescant"
    

if __name__ == "__main__":
    app.run()