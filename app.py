from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    then = datetime(2001, 9, 5)
    now = datetime.now()

    duration = now - then
    duration_in_s = duration.total_seconds()
    return render_template(
        "index.html", 
        minutes=divmod(duration_in_s, 60)[0], 
        days=duration.days)


if __name__ == "__main__":
    app.run()
