import pandas
import matplotlib.pyplot as plt

#create new dataframe of the raw data
bball= pandas.read_table('UWvMSU_1-22-13.txt',delim_whitespace=True)

#setting running cumulative scores for both teams
UWscore = [0]
MSUscore = [0]
time = [0]

#loop to match scores with teams
for i in range(0, bball.shape[0], 1):
    if bball.team[i] == 'UW':
        UWscore.append(UWscore[-1]+bball.score[i])
        MSUscore.append(MSUscore[-1])
    elif bball.team[i] == 'MSU':
        MSUscore.append(MSUscore[-1]+bball.score[i])
        UWscore.append(UWscore[-1])
    time.append(bball.time[i])

#Line plot of both teams where 'r-' is a red line for UW and 'g-' is a green line for MSU
plt.plot(time, UWscore, 'r-', time, MSUscore, 'g-')