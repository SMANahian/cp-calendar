from flask import Flask, make_response
from threading import Thread
from const import CALENDAR_ICS_FILE_PATH

app = Flask('')

@app.route('/')
def home():
    raw_bytes = ""
    with open(CALENDAR_ICS_FILE_PATH, 'rb') as r:
        for line in r:
            raw_bytes = raw_bytes + line
    response = make_response(raw_bytes)
    response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    return response

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_bot_alive():
    t = Thread(target=run)
    t.start()