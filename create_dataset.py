import pandas as pd
from plot_play import plot_play
import matplotlib.pyplot as plt
import os

def combine_games(path, event):
    temps = []
    for fname in os.listdir(path):
        temp = pd.read_csv(path+fname, index_col=[0])
        temp = temp.loc[temp['event'] == event]
        temps.append(temp)
    df = pd.concat(temps)
    return df

'''
game = pd.read_csv('Data/Tracking/tracking_gameId_2017101505.csv')
pbp = pd.read_csv('Data/plays.csv')

print(game.head())

plot_play(game, pbp, 2017101505, 58, snap=False)
'''

#combined = combine_games('Data/Tracking/')

