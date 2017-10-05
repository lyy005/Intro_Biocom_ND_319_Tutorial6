#load file
import pandas
file=pandas.read_csv("UWvMSU_1-22-13.txt",header=0,sep="\t")
#making a UW only table
UWscore=file[file.team == 'UW']
#making a MSU only table
MSUscore=file[file.team == 'MSU']
#cumulative sum of scores
new = UWscore['cum_sum'] = UWscore.score.cumsum()
new2 = MSUscore['cum_sum'] = MSUscore.score.cumsum()
import matplotlib.pyplot as plt
plt.plot(UWscore['time'], UWscore['cum_sum'], 'r-', MSUscore['time'], MSUscore['cum_sum'], 'g-')






