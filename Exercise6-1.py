#Early working of part 1-not complete or correct

import pandas
import matplotlib.pyplot as plt
bball=pandas.read_table('UWvMSU_1-22-13.txt',delim_whitespace=True)
UW=bball[bball.team=='UW']
MSU=bball[bball.team=='MSU']

plt.plot('UWscore','r-','MSUscore','g-')
