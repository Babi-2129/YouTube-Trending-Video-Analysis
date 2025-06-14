## This script performs sentiment analysis on YouTube video titles using the VADER sentiment analysis tool.
import pandas as pd
df_all = pd.read_csv("final_yt_merged.csv", encoding="ISO-8859-1")

# Importing necessary libraries for sentiment analysis
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    if not isinstance(text, str):
        return "Neutral"
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df_all["title_sentiment"] = df_all["title"].apply(get_sentiment)

# Displaying the count of each sentiment category in the title
print(df_all["title_sentiment"].value_counts())


#VISUALIZATION

# Visualizing the sentiment distribution of video titles
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.countplot(data=df_all, x="title_sentiment", palette="Set2", order=["Positive", "Neutral", "Negative"])
plt.title("Title Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Videos")
plt.show()

#sentiment vs view
sentiment_views = df_all.groupby("title_sentiment")["views"].mean().sort_values(ascending=False)
print(sentiment_views)

# Sentiment analysis by country
country_sent = df_all.groupby(["country", "title_sentiment"]).size().unstack().fillna(0)
print(country_sent)


# Correlation & Trend Analysis
# This script analyzes the correlation between various numerical columns in the YouTube video dataset.

num_cols = ["views", "likes", "dislikes", "comment_count"]
df_num = df_all[num_cols]

#check correlation matrix
corr_matrix = df_num.corr()
print(corr_matrix)

# Visualizing the correlation matrix
import seaborn as sns
import matplotlib.pyplot as plt

#plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix: Views, Likes, Dislikes, Comments")
plt.show()

# Visualizing the relationship between views and likes by country
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_all, x="likes", y="views", hue="country", alpha=0.5)
plt.title("Views vs Likes by Country")
plt.xscale("log")
plt.yscale("log")
plt.show()
