from flask import Flask, make_response
from threading import Thread
from const import CALENDAR_ICS_FILE_PATH

app = Flask('')

@app.route('/')
def home():
    response = make_response(open(CALENDAR_ICS_FILE_PATH).read())
    response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    return response

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_bot_alive():
    t = Thread(target=run)
    t.start()