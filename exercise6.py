#### EXERCISE 6 #####
#question 1

#load the dataset
import pandas
bball = pandas.read_csv("UWvMSU_1-22-13.txt", sep='\t', lineterminator='\r')

#create blank column totalscore
bball2=bball.assign(totalscore=0)
print bball2.head(n=5)


for i in range(0,len(bball2),1):
    if bball2.team[i]=="UW":
        print "science is fun"
    else:
        print "Dan smells"

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

