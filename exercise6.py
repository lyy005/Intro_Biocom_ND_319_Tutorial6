#### EXERCISE 6 #####
#question 1

#load the dataset
import pandas
import numpy
bball = pandas.read_csv("UWvMSU_1-22-13.txt", sep='\t', lineterminator='\r')

#create blank column totalscore
bball2=bball.assign(totalscore="")

#make blank lists
uw_list = []
msu_list = []

#fill lists - one for each team
for i in range(0,len(bball2),1):
    if bball2.team[i]=="UW":
        uw_list.append(i)
    else:
       msu_list.append(i)

#add total score columns UW
for i in range(len(uw_list)):
    if i == 0:
        bball2.loc[uw_list[i], "totalscore"] = bball2.score.loc[uw_list[i]]
    else:
        bball2.loc[uw_list[i], "totalscore"] =bball2.totalscore.loc[uw_list[i-1]] + bball2.score.loc[uw_list[i]]


#add total score msu
for i in range(len(msu_list)):
    if i == 0:
        bball2.loc[msu_list[i], "totalscore"] = bball2.score.loc[msu_list[i]]
    else:
        bball2.loc[msu_list[i], "totalscore"] =bball2.totalscore.loc[msu_list[i-1]] + bball2.score.loc[msu_list[i]]

print bball2

#jsut need to graph it!
#actual plot
#import matplotlib.pyplot as plt
#plt.plot(Time,ScoreMSU,'g-',Time,ScoreUW,'gray-')

#question 2

