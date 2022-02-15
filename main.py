from dotenv import load_dotenv
from clist_api import load_contests
from ical_setup import update_calendar
from keep_alive import keep_bot_alive
from time import sleep

load_dotenv()

def main():
    keep_bot_alive()

    while True:
        sleep(120)
        load_contests()
        update_calendar()


if __name__ == "__main__":
    main()