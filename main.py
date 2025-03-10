import flask
import pandas as pd
import matplotlib.pyplot as plt

app = flask.Flask(__name__)

@app.route("/")
def start():
    return flask.render_template("start.html")

@app.route("/player")
def player():
    df = pd.read_csv('ZZZ_StatisticsCC.csv', sep=';')
    df.plot(kind='scatter', x='Version', y="Active Player Count")

    plt.title("spēlētāju skaits katrā versijā")
    plt.xlabel("Release Date")
    plt.ylabel("Revenue")
    plt.yticks(rotation=90)
    plt.savefig('player_zzz.png')


    df1 = pd.read_csv('Game_StatisticsHSR (1).csv')
    df1.plot(kind='scatter', x='Version', y="Active Player Count")

    plt.title("spēlētāju skaits katrā versijā")
    plt.xlabel("Release Date")
    plt.ylabel("Revenue")
    plt.savefig('player_HSR.png')

    df2 = pd.read_csv('game_statisticsgenshinimpact.csv')
    df2.plot(kind='scatter', x='Version', y="Active Player Count")

    plt.title("spēlētāju skaits katrā versijā")
    plt.xlabel("Release Date")
    plt.ylabel("Revenue")
    plt.savefig('player_genshin.png')
    return flask.render_template("player.html")

@app.route("/sales")
def sales():
    return flask.render_template("sales.html")

@app.route("/voice")
def voice():
    return flask.render_template("voice.html")

@app.route("/stars")
def stars():
    return flask.render_template("stars.html")

app.run(debug=True)
