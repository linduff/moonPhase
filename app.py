from quart import Quart, render_template
from datetime import datetime
from astral import moon

app = Quart(__name__)

@app.route("/")
async def homepage():
    time_t = datetime.now()
    return await render_template("moonPhase.html", phase = "{:.3f}".format(moon.phase(time_t)))


if __name__ == "__main__":
    app.run()