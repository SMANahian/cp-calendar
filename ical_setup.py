import json
import icalendar
from icalendar import Calendar, Event, vDatetime
from datetime import datetime

from const import *


def update_calendar():
    cal = Calendar()
    cal.add('attendee', 'MAILTO:smanahian123@gmail.com')
    cal.add('summary', 'CP Contest Calendar')
    cal.add('version', '2.0')

    data = 0
    with open(CONTESTS_JSON_FILE_PATH) as f:
        data = json.load(f)
    
    tz = icalendar.cal.Timezone()
    tz.add('tzid', 'UTC')
    cal.add_component(tz)

    t = datetime.now()

    for contest in data['objects']:
        event = Event()
        event.add('summary', contest['event'])
        event.add('dtstart', vDatetime(datetime.strptime(contest['start'], "%Y-%m-%dT%H:%M:%S")))
        event.add('dtend', vDatetime(datetime.strptime(contest['end'], "%Y-%m-%dT%H:%M:%S")))
        event.add('last-modified', vDatetime(t))
        event.add('location', f"https://{contest['host']}")
        event.add('description', f"Contest Link: {contest['href']}")
        event.add('url', contest['href'])
        event.add('uid', contest['id'])
        cal.add_component(event)


    with open(CALENDAR_ICS_FILE_PATH, 'w') as f:
        f.write(str(cal.to_ical()).replace('\\r\\n', '\n').strip()[2:-1])



