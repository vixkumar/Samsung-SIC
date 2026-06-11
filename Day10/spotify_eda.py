import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

song = pd.read_csv(r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\spotify_global_2019_most_streamed_tracks_audio_features.csv")
song.head()
song.info()
song.describe()

df = song[["Rank", "Artist", "Track Name","Artist_popularity", "Streams", "tempo", "danceability", "energy"]]
df.head()

pop_song = df[df["Artist_popularity"] > 90]
print(pop_song.head())

rank = pop_song["Artist"].value_counts()
print(rank)
type(rank)

print(pop_song["Artist"].unique())

"BTS" in rank.index
bts = pop_song[pop_song["Artist"] == "BTS"]
print(bts.shape)

play_list = pop_song[pop_song["Artist"] == "Post Malone"]
Malone = play_list.reset_index(drop=True, inplace = False)

print(Malone)

x = pop_song["energy"]
y = pop_song["Rank"]
plt.scatter(x, y, color="red", alpha = 0.5)
plt.show()

pop_song.corr(method="pearson", numeric_only=True)
cor = pop_song.corr(method = "pearson", numeric_only=True)
cor
plt.matshow(cor)
plt.colorbar()
plt.show()
plt.figure(figsize=(8, 6))
sns.heatmap(cor, annot= True)
plt.show()


