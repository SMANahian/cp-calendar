import json
from turtle import done
import icalendar
from icalendar import Calendar, Event, vDatetime
from datetime import datetime

from const import CONTESTS_JSON_FILE_PATH


def get_event(contest, current_time):
    event = Event()
    event.add('summary', contest['event'])
    event.add('dtstart', vDatetime(datetime.strptime(contest['start'], "%Y-%m-%dT%H:%M:%S")))
    event.add('dtend', vDatetime(datetime.strptime(contest['end'], "%Y-%m-%dT%H:%M:%S")))
    event.add('last-modified', vDatetime(current_time))
    event.add('location', f"https://{contest['host']}")
    event.add('description', f"Contest Link: {contest['href']}")
    event.add('url', contest['href'])
    event.add('uid', contest['id'])
    
    return event

def load_contests_per_need(resources):
    cal = Calendar()
    cal.add('summary', 'CP Contest Calendar')
    cal.add('version', '2.0')

    tz = icalendar.cal.Timezone()
    tz.add('tzid', 'UTC')
    cal.add_component(tz)

    data = 0
    with open(CONTESTS_JSON_FILE_PATH) as f:
        data = json.load(f)

    current_time = datetime.now()

    for contest in data['objects']:
        if contest['resource_id'] in resources:
            done = False
            if resources['global'][1] != []:
                for gl_r_keyword in resources['global'][1]:
                    if (    gl_r_keyword in contest['href'].lower()
                        or gl_r_keyword in contest['event'].lower()
                    ):
                        done = True
                        break
            if not done and resources['global'][0] != []:
                for gl_a_keyword in resources['global'][0]:
                    if (    gl_a_keyword in contest['href'].lower()
                        or gl_a_keyword in contest['event'].lower()
                    ):
                        cal.add_component(get_event(contest, current_time))
                        done = True
                        break
            
            if not done and resources[contest['resource_id']][1] != []:
                for restricted_keyword in resources[contest['resource_id']][1]:
                    if (    restricted_keyword in contest['href'].lower()
                        or restricted_keyword in contest['event'].lower()
                    ):
                        done = True
                        break

            if not done:
                if resources[contest['resource_id']][0] == []:
                    cal.add_component(get_event(contest, current_time))
                    done = True
                    continue
                for allowed_keyword in resources[contest['resource_id']][0]:
                    if (    allowed_keyword in contest['href'].lower()
                        or allowed_keyword in contest['event'].lower()
                    ):
                        cal.add_component(get_event(contest, current_time))
                        done = True
                        break

    return str(cal.to_ical().decode('utf-8'))

