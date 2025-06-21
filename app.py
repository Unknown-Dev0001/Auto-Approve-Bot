from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bot working hai @BotVerseRavi'


if __name__ == "__main__":
    app.run()
