import sqlite3

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

conn = sqlite3.connect("data/sentiment_tracker.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())