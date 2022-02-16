import os

CONTESTS_JSON_FILE_PATH=os.path.join("files", "contests.json")
CALENDAR_ICS_FILE_PATH=os.path.join("files", "calendar.ics")
CLIST_API_TIME_DIFFERENCE=30 * 60 
URL_BASE = 'https://clist.by/api/v2/contest/'
RESOURCES = {
    "global": ([], ["registration"]),
    2: (["all"], []),
    64: (["all"], []),
    35: (["all"], []),
    93: (["abc", "arc", "agc"], []),
    12: (["srm"], []),
}