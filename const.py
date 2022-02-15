import os

CONTESTS_JSON_FILE_PATH=os.path.join("files", "contests.json")
CALENDAR_ICS_FILE_PATH=os.path.join("files", "calendar.ics")
CLIST_API_TIME_DIFFERENCE=30 * 60 
URL_BASE = 'https://clist.by/api/v2/contest/'
RESOURCES = [
    "codechef.com",
    "codeforces.com",
    "codingcompetitions.withgoogle.com",
    "atcoder.jp",
    "topcoder.com",
]