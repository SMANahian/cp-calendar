from dotenv import load_dotenv
from clist_api import load_contests, load_resources
from website import create_app
from time import sleep
from threading import Thread

load_dotenv()
app = create_app()


def run():
    app.run(host='0.0.0.0',port=8080)


def main():
    server = Thread(target=run)
    server.start()

    while True:
        load_resources()
        load_contests()
        sleep(1800)


if __name__ == "__main__":
    main()