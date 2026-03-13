import sqlite3
import pandas as pd

DB_PATH = "data/sentiment_tracker.db"
DB_PATH_RAW = "data/rawdata.db"

def create_table():
    connection = sqlite3.connect("data/sentiment_tracker.db")
    cursor = connection.cursor()
    command1 = """
    CREATE TABLE IF NOT EXISTS sentiment (
    date TEXT,
    topic TEXT,
    title_weight REAL,
    description_weight REAL,
    caption_weight REAL,
    sentiment_mean REAL,
    positive_ratio REAL,
    price REAL,
    PRIMARY KEY (date, topic, title_weight, description_weight, caption_weight)
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

def insert_sentiment(date, topic, sentiment_mean, positive_ratio, price, title_weight, description_weight, caption_weight):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO sentiment
        (date, topic, sentiment_mean, positive_ratio, price, title_weight, description_weight, caption_weight)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (date, topic, sentiment_mean, positive_ratio, price, title_weight, description_weight, caption_weight),
    )

    connection.commit()
    connection.close()

def insert_raw(date, topic, video_id, title_score, desc_score, cap_score):
    connection = sqlite3.connect(DB_PATH_RAW)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO raw
        (date, topic, video_id, title_score, description_score, caption_score)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (date, topic, video_id, title_score, desc_score, cap_score),
    )

    connection.commit()
    connection.close()


import pandas as pd

# --- use the following to print the db storing the data to see how they look --- 

# conn = sqlite3.connect("data/sentiment_tracker.db")
# conn2 = sqlite3.connect("data/rawdata.db")

# cursor = conn.cursor()

# df_sentiment = pd.read_sql_query("SELECT * FROM sentiment", conn)
# df_raw = pd.read_sql_query("SELECT * FROM raw", conn2)

# print(df_sentiment)
# print("----------")
# print(df_raw)

# conn.close()
# conn2.close()

# ---Use the following to delete a table---
# make sure to change table name to which one you want to delete
# sentiment for aggregate data, raw for raw data

# connection = sqlite3.connect("data/sentiment_tracker.db")
# cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS sentiment")

# connection.commit()
# connection.close()

