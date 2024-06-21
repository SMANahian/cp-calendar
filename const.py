import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
CONTESTS_JSON_FILE_PATH=os.path.join(APP_ROOT, "files", "contests.json")
RESOURCES_JSON_FILE_PATH=os.path.join(APP_ROOT, "files", "resources.json")
CLIST_API_TIME_DIFFERENCE=30 * 60
CONTESTS_URL_BASE = 'https://clist.by/api/v2/contest/'
RESOURCES_URL_BASE = 'https://clist.by/api/v2/resource/'
RESOURCES = {
    "global": ([], ["registration"]),
    2: ([], []),
    64: ([], []),
    35: ([], []),
    93: (["abc", "arc", "agc"], []),
    12: (["srm"], []),
}