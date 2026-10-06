import pandas as pd

print("part 1 pandas series")
scores = [98500,87500, 95000, 100000, 105000]
players = pd.Series(scores, index = ['the_hunter565', 'night_fox', '89pixel_king', 'knight_riders', 'energetic_toad'])
print(players)

print("\npart 2 pandas dataframe")
data = {
    'player': ['the_hunter565', 'night_fox', '89pixel_king', 'knight_riders', 'energetic_toad'],
    'level': [89, 34, 67, 56, 45],
    'score': [98500, 87500, 95000, 100000, 105000],
    'wins': [10, 5, 15, 8, 12]
}
df = pd.DataFrame(data)
print(df)
print("\npart 3 accessing rows")
print("row 0 (top player):")
print(df.iloc[0])
print()
print('rows 2 and 3:')
print(df.iloc[1:3])
print()
print("part 4  reading a CSV file ")
full_df = pd.read_csv('leaderboard.csv')
print("first 5 rows (head):")
print(full_df.head())
print("last 3 rows (tail):")
print(full_df.tail(3))
print()
print("dataset info:")
print(full_df.info())

print("part 5 cleaning data")
print("rows with missing values removed(dropna):")
print(full_df.dropna())
print("rows with missing values filled (fillna):")
filled_df = full_df.fillna(0)
print(filled_df)