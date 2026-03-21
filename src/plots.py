import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conn = sqlite3.connect("data/sentiment_tracker.db")
df_sentiment = pd.read_sql_query("SELECT * FROM sentiment", conn)
conn.close()

df_sentiment["date"] = pd.to_datetime(df_sentiment["date"])

# Filter by topic
df_topicbtc = df_sentiment[df_sentiment["topic"] == "bitcoin"].copy()
df_topicnvda = df_sentiment[df_sentiment["topic"] == "nvidia"].copy()

# Filter by one weighting scheme
df_topicbtc = df_topicbtc[
    (df_topicbtc["title_weight"] == 0.9) &
    (df_topicbtc["description_weight"] == 0.1) &
    (df_topicbtc["caption_weight"] == 0.0)
].copy()

df_topicnvda = df_topicnvda[
    (df_topicnvda["title_weight"] == 0.9) &
    (df_topicnvda["description_weight"] == 0.1) &
    (df_topicnvda["caption_weight"] == 0.0)
].copy()

# Sort by date
df_topicbtc = df_topicbtc.sort_values("date")
df_topicnvda = df_topicnvda.sort_values("date")

# Print data for checking
print("Bitcoin:")
print(df_topicbtc[["date", "topic", "sentiment_mean"]])

print("\nNVDA:")
print(df_topicnvda[["date", "topic", "sentiment_mean"]])

# Plot Bitcoin
plt.figure(figsize=(10, 5))
plt.plot(df_topicbtc["date"], df_topicbtc["sentiment_mean"], marker="o")
plt.xlabel("Date")
plt.ylabel("Sentiment Mean")
plt.title("Bitcoin Sentiment Over Time")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot NVDA
plt.figure(figsize=(10, 5))
plt.plot(df_topicnvda["date"], df_topicnvda["sentiment_mean"], marker="o")
plt.xlabel("Date")
plt.ylabel("Sentiment Mean")
plt.title("NVDA Sentiment Over Time")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()