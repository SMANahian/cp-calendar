import os
import datetime
import requests
import json
from pathlib import Path


from const import URL_BASE, CONTESTS_JSON_FILE_PATH, RESOURCES, CLIST_API_TIME_DIFFERENCE


class ClistApiError(Exception):
    """Base class for all API related errors."""

    def __init__(self, message=None):
        super().__init__(message or 'Clist API error')


class ClientError(Exception):
    """An error caused by a request to the API failing."""

    def __init__(self):
        super().__init__('Error connecting to Clist API')


def _query_api():
    clist_token = os.getenv('CLIST_API_TOKEN')
    contests_start_time = datetime.datetime.utcnow() - datetime.timedelta(days=7)
    contests_start_time_string = contests_start_time.strftime("%Y-%m-%dT%H%%3A%M%%3A%S")
    url = URL_BASE + '?limit=200&start__gte=' + contests_start_time_string + '&' + clist_token

    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            raise ClistApiError
        return resp.json()['objects']
    except Exception as e:
        raise ClientError from e


def load_contests(forced=False):
    current_time_stamp = datetime.datetime.utcnow().timestamp()
    db_file = 0
    db_file = Path(CONTESTS_JSON_FILE_PATH)

    db = None
    try:
        with db_file.open() as f:
            db = json.load(f)
    except BaseException:
        pass

    last_time_stamp = db['querytime'] if db and db['querytime'] else 0

    if not forced and current_time_stamp - last_time_stamp < CLIST_API_TIME_DIFFERENCE:
        return

    contests = _query_api()
    db = {}
    db['querytime'] = current_time_stamp



    db['objects'] = contests
    with open(db_file, 'w') as f:
        json.dump(db, f, indent=4)
