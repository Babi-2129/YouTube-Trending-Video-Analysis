import pandas as pd

# This script reads YouTube video data from CSV files for different countries and stores them in pandas DataFrames.
df_in = pd.read_csv("INvideos.csv", encoding='ISO-8859-1')
df_kr = pd.read_csv("KRvideos.csv", encoding='ISO-8859-1')
df_jp = pd.read_csv("JPvideos.csv", encoding='ISO-8859-1')

# Adding a new column 'country' to each DataFrame to indicate the country of the videos
df_in["country"] = "IN"
df_kr["country"] = "KR"
df_jp["country"] = "JP"

# Concatenating all DataFrames into a single DataFrame
df_all = pd.concat([df_in, df_kr, df_jp], ignore_index=True)

# Displaying the shape and columns of the combined DataFrame
print("Shape:", df_all.shape)
print("Columns:", df_all.columns.tolist())
df_all.head()

# Converting 'trending_date' and 'publish_time' columns to datetime format
df_all["trending_date"] = pd.to_datetime(df_all["trending_date"], format="%y.%d.%m", errors='coerce')
df_all["publish_time"] = pd.to_datetime(df_all["publish_time"], errors='coerce')

# Dropping rows with NaN values in 'trending_date' and 'publish_time'
df_all.drop_duplicates(inplace=True)

# -------------------------------
# PHASE 2: Univariate & Category EDA
# -------------------------------

# Top 10 videos by views across all countries
top_videos = df_all.sort_values(by="views", ascending=False).head(10)
top_videos[["title", "channel_title", "views", "country"]]

# Most popular categories by countries
df_all.groupby(["country", "category_id"])["views"].mean().reset_index().sort_values(by="views", ascending=False)

# Most liked and disliked videos across all countries
top_liked = df_all.sort_values(by="likes", ascending=False).head(5)
top_disliked = df_all.sort_values(by="dislikes", ascending=False).head(5)

#visualization of views distribution
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.histplot(df_all["views"], bins=50, kde=True)
plt.title("Views Distribution")
plt.xscale("log")
plt.show()

#country wise video count
df_all["country"].value_counts()


# -------------------------------
# PHASE 3: Mapping & Visualization
# ------------------------------- 

#Mapping category IDs to their respective names
category_mapping = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    18: "Short Movies",
    19: "Travel & Events",
    20: "Gaming",
    21: "Videoblogging",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "Howto & Style",
    27: "Education",
    28: "Science & Technology",
    29: "Nonprofits & Activism",
    30: "Movies",
    31: "Anime/Animation",
    32: "Action/Adventure",
    33: "Classics",
    34: "Documentary",
    35: "Drama",
    36: "Family",
    37: "Foreign",
    38: "Horror",
    39: "Sci-Fi/Fantasy",
    40: "Thriller",
    41: "Shorts",
    42: "Shows",
    43: "Trailers"
}

#Applying the data to the DataFrame to create a new column 'category_name'
df_all["category_name"] = df_all["category_id"].map(category_mapping)

#Priviewing Result
print("Shape:", df_all.shape)
print("Columns:", df_all.columns)

# Saving the final DataFrame to a CSV file
df_all.to_csv("final_yt_merged.csv", index=False, encoding="ISO-8859-1")


