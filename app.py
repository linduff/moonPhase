from flask import Flask, render_template, redirect, jsonify
from datetime import datetime
from astral import moon
import asciiMoonPhases as asciiMoon

app = Flask(__name__)

@app.route("/")
def whatPhaseIsTheMoon():
    current_date = datetime.now()
    phaseNumber = moon.phase(current_date)
    phaseName, phaseArt = getPhaseNameAndArt(phaseNumber)
    return render_template("moonPhase.html", phaseNumber = "{:.3f}".format(phaseNumber), phaseName = phaseName, phaseArt = phaseArt)

@app.route('/healthcheck')
def health():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

def getPhaseNameAndArt(phaseNumber):
    if phaseNumber < 0.5 or phaseNumber > 27.5:
        return "New Moon", asciiMoon.mewMoon
    elif phaseNumber >= 0.5 and phaseNumber <= 6.5:
        return "Waxing Crescant", asciiMoon.waxingCrescent
    elif phaseNumber > 6.5 and phaseNumber < 7.5:
        return "First Quarter", asciiMoon.firstQuarter
    elif phaseNumber >= 7.5 and phaseNumber <= 13.5:
        return "Waxing Gibbous", asciiMoon.waxingGibbous
    elif phaseNumber > 13.5 and phaseNumber < 14.5:
        return "Full Moon", asciiMoon.fullMoon
    elif phaseNumber >= 14.5 and phaseNumber <= 20.5:
        return "Waning Gibbous", asciiMoon.waningGibbous
    elif phaseNumber > 20.5 and phaseNumber < 21.5:
        return "Third Quarter", asciiMoon.thirdQuarter
    else:
        return "Waning Crescant", asciiMoon.waningCrescent
    

if __name__ == "__main__":
    app.run()