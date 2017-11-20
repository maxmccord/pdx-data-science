import pandas as pd
import matplotlib.pyplot as plt

from board_game_data import Titles,Users

# Returns a dataframe with the mean ratings of every game.
def mean_ratings(data, titles=False):
   means = data.groupby('game_id').mean()['rating']
   return means if not titles else pd.DataFrame({'title': Titles.get(), 'mean_rating': means})

# Returns a dataframe with the median ratings of every game.
def median_ratings(data, titles=False):
   medians = data.groupby('game_id').median()['rating']
   return medians if not titles else pd.DataFrame({'title': Titles.get(), 'median_rating': medians})

# Plots overlapping histograms of the mean ratings of every game in all three
# of the data sets.
def plot_dataset_histograms():
   mean_ratings(Users.frequent()).plot.hist(bins=50, alpha=0.4, label='frequent')
   mean_ratings(Users.all()).plot.hist(bins=50, alpha=0.4, label='all')
   mean_ratings(Users.elite()).plot.hist(bins=50, alpha=0.4, label='elite')
   plt.title('Mean Rating Frequencies (50 bins)')
   plt.legend(loc='upper right')
   plt.show()

# Returns a correlation matrix for all users.
def correlation(data):
   return data.pivot('game_id', 'user_id', 'rating').corr();

# Given a correlation matrix and one user ID, returns a Series of correlation
# values between that user and all other users, sorted in descending order.
def sorted_correlated_users(corr_matrix, userId):
   return corr_matrix[userId].sort_values(ascending=False).reset_index()['user_id']

# Creates a scatter plot of ratings, where each point represents a game that
# both users voted on.
def plot_ratings_user_vs_user(user1, user2, data):
   # rearrange data frame so that User IDs are on the columns
   ratings = data.pivot(index='game_id', columns='user_id', values='rating')

   # take only the two users of interest, and only use games that both voted on
   ratings = ratings[[user1, user2]].dropna()
   ratings = ratings.rename(index=str, columns={user1 : 'user1', user2 : 'user2'})

   # user1 rating on x-axis, user2 rating on y-axis
   ratings.plot(x='user1', y='user2', kind='scatter', alpha=0.2)
   plt.title('Correlation between %d and %d' % (user1, user2))

# Program entry point
def main():
   user = 173971
   data = Users.elite()

   user_correlations = sorted_correlated_users(correlation(data), user)

   top_user = user_correlations.iloc[1]
   bottom_user = user_correlations.iloc[-20]

   plot_ratings_user_vs_user(user, top_user, data)
   plt.title('High Correlation')
   plot_ratings_user_vs_user(user, bottom_user, data)
   plt.title('Low Correlation')
   plt.show()


if __name__ == '__main__':
   main()
