import pandas
import matplotlib.pyplot as plt

game = pandas.read_table('UWvMSU_1-22-13.txt')

game = game.assign(UWscore = 0)
game = game.assign(MSUscore = 0)

print(game)
