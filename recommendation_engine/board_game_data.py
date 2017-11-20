import pandas as pd

# Constants
DATA_GAME_TITLES    = 'data/boardgame-titles.csv'
DATA_ELITE_USERS    = 'data/boardgame-elite-users.csv'
DATA_FREQUENT_USERS = 'data/boardgame-frequent-users.csv'
DATA_ALL_USERS      = 'data/boardgame-users.csv'

# Singleton for accessing title data.
class Titles():
   _titles = None

   def get():
      if Titles._titles is None:
         # NOTE: "squeeze" means that read_csv will return a Series if the resulting
         # DataFrame only contains 1 column.
         Titles._titles = pd.read_csv(DATA_GAME_TITLES, index_col=0, squeeze=True)
      return Titles._titles

# Singleton methods for accessing user data.
class Users():
   _elite = _frequent = _all = None

   def elite():
      if Users._elite is None:
         Users._elite = pd.read_csv(DATA_ELITE_USERS)
      return Users._elite

   def frequent():
      if Users._frequent is None:
         Users._frequent = pd.read_csv(DATA_FREQUENT_USERS)
      return Users._frequent

   def all():
      if Users._all is None:
         Users._all = pd.read_csv(DATA_ALL_USERS)
      return Users._all
