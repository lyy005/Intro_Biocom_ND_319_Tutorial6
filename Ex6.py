import os

os.getcwd()
os.chdir("Intro_Biocom_ND_319_Tutorial6/")

import pandas
import numpy

game = pandas.read_table("UWvMSU_1-22-13.txt", sep="\t")

import matplotlib.pyplot as plt

WiscScore = game.loc[game['team'] == 'UW', ['score']]
MSUscore = game.loc[game['team'] == 'MSU', ['score', 'time']]

plt.plot(WiscScore.time, WiscScore,'r-', MSUscore.time,MSUscore,'g-')

### alternatively ###

import plotnine as p9

x = p9.ggplot(game, aes(x='time', y='score', color = 'factor(team)'))
x+geom_line()


### Q2 ###

N = numpy.random.choice(100)

guess = int(input("Guess: "))

tries = 1

while guess != N and tries < 100:
    if guess < N:
        print("Higher!")
    elif guess > N:
        print("Lower!")
    guess = int(input("Guess: "))

if guess == N:
    print("Correct!")
    

