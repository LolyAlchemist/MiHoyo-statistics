import flask
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

app = flask.Flask(__name__)

def init_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                answer TEXT NOT NULL
            )
        """)
        conn.commit()
init_db()

def init2_db():
    conn = sqlite3.connect("atbilde.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            response TEXT CHECK(response IN ('Yes', 'No')) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init2_db()

def save_atbilde(atbilde):
    conn = sqlite3.connect("atbilde.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO responses (response) VALUES (?)", (atbilde,))
    conn.commit()
    conn.close()



@app.route("/", methods=["GET", "POST"])
def start():
    if flask.request.method == "POST":
        answer = flask.request.form["answer"]

        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO answers (answer) VALUES (?)", (answer,))
            conn.commit()
        return flask.redirect("/")


    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM answers")
        answers = cursor.fetchall()

    return flask.render_template("start.html", answers=answers)


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
        "Version": ["4.0", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "5.0", "5.2", "5.3"],
        "Revenue": [
            "$4.5B", "$4.7B", "$4.8B", "$5B", 
            "$5.1B", "$5.2B", "$5.3B", "$5.4B", 
            "$5.5B", "$1.56B", "$5.6B", "$5.7B"
        ]
    }

    df3 = pd.DataFrame(data1)

    revenue_values = [4.5, 4.7, 4.8, 5, 5.1, 5.2, 5.3, 5.4, 5.5 , 1.56, 5.6, 5.7]
    df3['Revenue Values'] = revenue_values


    df3.plot(y='Revenue Values', kind='pie', labels=df3['Version'], startangle=90, autopct='%1.1f%%', figsize=(8, 8))

    plt.title('Ieņēmumu sadalījums pēc versijas')
    plt.ylabel('') 
    plt.savefig('static/images/sales_genshin.png')

    data2 = {
        "Version": ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "2.0", "2.1", "2.2", "2.3", "2.7", "3.0"],
        "Revenue": [
        "$60M)", "$400M", "$600M", "$700M", 
        "$865M", "$1000M", "$1200M", 
        "$1400M", "$1600M", "$1800M", 
        "$2000M", "$2100M", "$2300M"
        ]
    }


    df4 = pd.DataFrame(data2)

    revenue_values = [60, 400, 600, 700, 865, 1000, 1200, 1400, 1600, 1800, 2000, 2100, 2300]
    df4['Revenue Values'] = revenue_values
    df4.plot(y='Revenue Values', kind='pie', labels=df4['Version'], startangle=90, autopct='%1.1f%%', figsize=(8, 8))


    plt.title('Ieņēmumu sadalījums pēc versijas')
    plt.ylabel('')
    plt.savefig('static/images/sales_HSR.png')

    data3 = {
        "Version": ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5"],
        "Revenue": [
        "100M", "$67M", "Not specified", 
        "Not specified", "250M", "Not specified"
        ]
        }
    df5 = pd.DataFrame(data3)
    revenue_values = [100, 67, 0, 0, 250, 0]
    df5['Revenue'] = revenue_values
    df5.plot(y='Revenue', kind='pie', labels=df5['Version'], startangle=90, autopct='%1.1f%%', figsize=(8, 8))
    plt.title('Ieņēmumu sadalījums pēc versijas')
    plt.ylabel('')
    plt.savefig('static/images/sales_zzz.png')



    return flask.render_template("sales.html")


@app.route("/stars", methods=["GET", "POST"])
def stars():
    hsr_df = pd.read_csv('static\Honakai_Star_Rail_CharLIST.csv')

    he_df = hsr_df.head(10)
    he_df.hist(column="Name", by="Star Rarity", bins=30)
    plt.savefig('static/images/stars_hsr.png')
    ye_df = hsr_df.tail(10)
    ye_df.hist(column="Name", by="Star Rarity", bins=30)
    plt.savefig('static/images/starsT_hsr.png')

    gg_df = pd.read_csv('static\Genshin_Character_List.csv')
    ihwa_df = gg_df.head(10)
    ihwa_df.hist(column="Name", by="Star Rarity", bins=30)
    plt.savefig('static/images/starsH_gii.png')

    ihwa2_df = gg_df.tail(10)
    ihwa2_df.hist(column="Name", by="Star Rarity", bins=30)
    plt.savefig('static/images/starsT_gi2.png')



    message = ""

    if flask.request.method == "POST":
        atbilde = flask.request.form["response"]
        save_atbilde(atbilde)
        message = "Paldies par atbildi!"
    
    return flask.render_template("stars.html", message= message )





app.run(debug=True)
