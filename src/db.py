import sqlite3
import pandas as pd

DB_PATH = "data/sentiment_tracker.db"

def create_table():
    connection = sqlite3.connect("data/sentiment_tracker.db")
    cursor = connection.cursor()
    command1 = """
    CREATE TABLE IF NOT EXISTS sentiment (
    date TEXT,
    topic TEXT,
    sentiment_mean REAL,
    positive_ratio REAL,
    price REAL,
    PRIMARY KEY (date, topic)
    )
    """
    cursor.execute(command1)
    connection.commit()
    connection.close()

def create_table_raw():
    connection = sqlite3.connect("data/rawdata.db")
    cursor = connection.cursor()
    command1 = """
    CREATE TABLE IF NOT EXISTS raw (
    date TEXT,
    topic TEXT,
    video_id TEXT,
    title_score REAL,
    description_score REAL,
    caption_score REAL, 
    PRIMARY KEY (date, topic, video_id)
    )
    """
    cursor.execute(command1)
    connection.commit()
    connection.close()

def insert_sentiment(date, topic, sentiment_mean, positive_ratio, price):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO sentiment
        (date, topic, sentiment_mean, positive_ratio, price)
        VALUES (?, ?, ?, ?, ?)
        """,
        (date, topic, sentiment_mean, positive_ratio, price),
    )

    connection.commit()
    connection.close()


import pandas as pd

conn = sqlite3.connect("data/sentiment_tracker.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM sentiment WHERE topic='bitcoin'")
conn.commit()

df = pd.read_sql_query("SELECT * FROM sentiment", conn)

print(df)

conn.close()

