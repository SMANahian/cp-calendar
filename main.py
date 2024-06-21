from dotenv import load_dotenv
from website import create_app
from threading import Thread

load_dotenv()
app = create_app()


def run():
    app.run(host='0.0.0.0',port=8080)


def main():
    server = Thread(target=run)
    server.start()


if __name__ == "__main__":
    main()