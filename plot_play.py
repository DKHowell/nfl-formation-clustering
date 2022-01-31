import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#create a football field plot.
#https://www.kaggle.com/robikscube/nfl-big-data-bowl-plotting-player-position
def create_football_field(xscale=1,
                          linenumbers=True,
                          endzones=True,
                          highlight_line=False,
                          highlight_line_number=50,
                          highlighted_name=None,
                          fifty_is_los=False,
                          figsize=(12, 6.33)):
    """
    Function that plots the football field for viewing plays.
    Allows for showing or hiding endzones.
    """
    rect = patches.Rectangle((0, 0), 120, 53.3, linewidth=0.1,
                             edgecolor='r', facecolor='darkgreen', zorder=0)

    fig, ax = plt.subplots(1, figsize=figsize)
    ax.add_patch(rect)

    plt.plot([10, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
              80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
             [0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3,
              53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
             color='white')
    if fifty_is_los:
        plt.plot([60, 60], [0, 53.3], color='gold')
        plt.text(62, 50, '<- Player Yardline at Snap', color='gold')
    # Endzones
    if endzones:
        ez1 = patches.Rectangle((0, 0), 10, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='blue',
                                alpha=0.2,
                                zorder=0)
        ez2 = patches.Rectangle((110, 0), 120, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='blue',
                                alpha=0.2,
                                zorder=0)
        ax.add_patch(ez1)
        ax.add_patch(ez2)
    plt.xlim(0, 120)
    plt.ylim(-5, 58.3)
    plt.axis('off')
    if linenumbers:
        for x in range(20, 110, 10):
            numb = x
            if x > 50:
                numb = 120 - x
            plt.text(x, 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='white')
            plt.text(x-0.8*xscale, 53.3 - 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='white', rotation=180)
    if endzones:
        hash_range = range(11, 110)
    else:
        hash_range = range(1, 120)

    for x in hash_range:
        ax.plot([x, x], [0.4, 0.7], color='white')
        ax.plot([x, x], [53.0, 52.5], color='white')
        ax.plot([x, x], [22.91, 23.57], color='white')
        ax.plot([x, x], [29.73, 30.39], color='white')

    if highlight_line:
        hl = highlight_line_number + 10
        plt.plot([hl, hl], [0, 53.3], color='yellow')
        if highlighted_name:
            plt.text(hl + 2, 50, '<- {}'.format(highlighted_name), color='yellow')
    return fig, ax

#plot defense on the football field
def plot_defense(df, gameid, playid):
    play = df.loc[(df['gameId'] == gameid) & (df['playId'] == playid)]
    yl = play['yardlineNumber'].tolist()[0]
    yl = 100-yl
    xmin = play['x'].min()
    xmax = play['x'].max()
    xscale = (xmax-xmin+10)/120
    fig, ax = create_football_field(xscale=xscale,  highlight_line=True,
                                    highlight_line_number=yl)
    play.plot(x='x', y='y', kind='scatter', ax=ax, color='red', s=size, zorder=1)
    plt.xlim(xmin-5, xmax+5)
    for i in range(play.shape[0]):
        plt.text(x=play.loc[play.index[i], 'x']-xscale,\
                 y=play.loc[play.index[i], 'y']-1,\
                 s=int(play.loc[play.index[i], 'jerseyNumber']), c='white', weight='bold')
    plt.title(f'Game #{gameid}\nPlay #{playid}')
    plt.show()
    #plt.savefig('demoplay_move.png')

#plot player position on football field based on gameID and playID
#if snap==True, will only plot positions at the moment of the snap
def plot_play(df, game_data, gameid, playid, snap = True):
    yl = game_data.query("gameId == @gameid and playId == @playid")['yardlineNumber'].tolist()[0]
    yl = 100-yl
    play = df.query(f"gameId == {gameid} and playId == {playid}")
    if snap:
        play = play.loc[play['event'] == 'ball_snap']
        size = 150
    else:
        size = 10
    home = play.loc[play['team'] == 'home']
    away = play.loc[play['team'] == 'away']
    xmin = play['x'].min()
    xmax = play['x'].max()
    xscale = (xmax-xmin+10)/120
    fig, ax = create_football_field(xscale=xscale,  highlight_line=True,
                                    highlight_line_number=yl)
    home.plot(x='x', y='y', kind='scatter', ax=ax, color='red', s=size, zorder=1)
    away.plot(x='x', y='y', kind='scatter', ax=ax, color='steelblue', s=size, zorder=1)
    plt.xlim(xmin-5, xmax+5)
    if snap:
        for i in range(home.shape[0]):
            plt.text(x=home.loc[home.index[i], 'x']-xscale,\
                     y=home.loc[home.index[i], 'y']-1,\
                     s=int(home.loc[home.index[i], 'jerseyNumber']), c='white', weight='bold')
            plt.text(x=away.loc[away.index[i], 'x']-xscale,\
                     y=away.loc[away.index[i], 'y']-1,\
                     s=int(away.loc[away.index[i], 'jerseyNumber']), c='white', weight='bold')
    plt.title(f'Game #{gameid}\nPlay #{playid}')
    plt.show()