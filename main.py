import flask
import pandas as pd
import matplotlib.pyplot as plt

app = flask.Flask(__name__)

@app.route("/")
def start():
    return flask.render_template("start.html")

@app.route("/player")
def player():
    df = pd.read_csv('static/ZZZ_StatisticsCC.csv', sep=';')
    df.plot(kind='scatter', x='Version', y="Active Player Count")

    plt.title("spēlētāju skaits katrā versijā")
    plt.xlabel("Release Date")
    plt.ylabel("Revenue")
    plt.yticks(rotation=90)
    plt.savefig('static/images/player_zzz.png')


    df1 = pd.read_csv('static/Game_StatisticsHSR (1).csv')
    df1.plot(kind='scatter', x='Version', y="Active Player Count")

    plt.title("spēlētāju skaits katrā versijā")
    plt.xlabel("Release Date")
    plt.ylabel("Revenue")
    plt.savefig('static/images/player_HSR.png')

    df2 = pd.read_csv('static/game_statisticsgenshinimpact.csv')
    df2.plot(kind='scatter', x='Version', y="Active Player Count")

    plt.title("spēlētāju skaits katrā versijā")
    plt.xlabel("Release Date")
    plt.ylabel("Revenue")
    plt.savefig('static/images/player_genshin.png')
    return flask.render_template("player.html")

@app.route("/sales")
def sales():
    data1 = {
    "Version": ["1.0", "01.janv", "01.febr", "01.marts", "01.apr", "01.maijs"],
    "Release Date": ["July 4, 2024", "15.aug.24", "September 26, 2024", "November 7, 2024", "December 18, 2024", "January 22, 2025"],
    "Active Player Count": ["50 million", "Not specified", "Not specified", "Not specified", "Not specified", "Not specified"],
    "Revenue": ["$50M in 11 days; $100M in first month", "$32.5M in August 2024; $34.5M in September 2024", "Not specified", "Not specified", "$8.6M daily; $250M total", "Not specified"],
    "In-Game Purchases": ["Initial in-game purchase offerings", "Special banners led to increased purchases", "New in-game items and features", "Additional in-game content and purchase options", 
                          "New characters, banners, and events introduced", "New outfits and Signal Searches introduced"]
}

    df3 = pd.DataFrame(data1)

    revenue_values = [50, 32.5, 0, 0, 250, 0]
    df3['Revenue Values'] = revenue_values


    df3.plot(y='Revenue Values', kind='pie', labels=df3['Version'], startangle=90, autopct='%1.1f%%', figsize=(8, 8))

    plt.title('Ieņēmumu sadalījums pēc versijas')
    plt.ylabel('') 
    plt.savefig('static/images/sales_genshin.png')



    return flask.render_template("sales.html")


@app.route("/stars")
def stars():
    return flask.render_template("stars.html")

app.run(debug=True)
