from flask import Flask, make_response
from threading import Thread
from const import RESOURCES
from ical_setup import load_contests_per_need

app = Flask('')

@app.route('/')
def home():
    s = load_contests_per_need(RESOURCES)
    print(s)
    response = make_response(s)
    response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    return response

@app.route('/calendar/')
def calendar():
    pass

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_bot_alive():
    t = Thread(target=run)
    t.start()