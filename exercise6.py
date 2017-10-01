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
print uw_list
print msu_list

#add total score columns UW
for i in range(len(uw_list)):
    print(uw_list[i])
    if i == 0:
        bball2.loc[uw_list[i], "totalscore"] = bball2.score.loc[uw_list[i]]
    else:
        bball2.loc[uw_list[i], "totalscore"] =bball2.totalscore.loc[uw_list[i-1]] + bball2.score.loc[uw_list[i]]


#add total score msu
for i in range(len(msu_list)):
    print(msu_list[i])
    if i == 0:
        bball2.loc[msu_list[i], "totalscore"] = bball2.score.loc[msu_list[i]]
    else:
        bball2.loc[msu_list[i], "totalscore"] =bball2.totalscore.loc[msu_list[i-1]] + bball2.score.loc[msu_list[i]]

print bball2




#for x in uw list:
# forthe second value bball2.totalscore[i]= bball2.totalscore[i-1] + bball2.score[i]


#Steps remaining:
#print times in the Time column of B
#create a running cumulative score for each team in B
#pseudocode (doesn't work)

#Create blank dataframe
#import numpy
#A=numpy.zeros((50,3))
#B=pandas.DataFrame(A,columns=['Time','ScoreMSU','ScoreUW'])
#Time = bball.time

#actual plot
#import matplotlib.pyplot as plt
#plt.plot(Time,ScoreMSU,'g-',Time,ScoreUW,'gray-')

#question 2

