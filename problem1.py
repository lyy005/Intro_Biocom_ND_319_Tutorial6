import pandas
import matplotlib.pyplot as plt

game = pandas.read_table('UWvMSU_1-22-13.txt')

game = game.assign(UWscore = 0)
game = game.assign(MSUscore = 0)


if game.loc[0,'team'] == 'UW':
    game.loc[0,'UWscore'] += game.loc[0,'score']
if game.loc[0,'team'] == 'MSU':
    game.loc[0,'MSUscore'] += game.loc[0,'score']
    
for row in range(1, len(game)):
    game.loc[row,'UWscore'] = game.loc[row - 1, 'UWscore']
    game.loc[row,'MSUscore'] = game.loc[row - 1, 'MSUscore']
    
    if game.loc[row,'team'] == 'UW':
        game.loc[row,'UWscore'] += game.loc[row,'score']
    if game.loc[row,'team'] == 'MSU':
        game.loc[row,'MSUscore'] += game.loc[row,'score']

plt.plot(game.time,game.UWscore,'-r',game.time,game.MSUscore,'-b')

#print(len(game))

#print(game)
