from dotenv import load_dotenv
from clist_api import load_contests, load_resources
from website import create_app
from time import sleep
from threading import Thread

load_dotenv()

def main():
    app = create_app()
    server = Thread(target=app.run)
    server.start()

    while True:
        load_resources()
        load_contests()
        sleep(1800)


if __name__ == "__main__":
    main()