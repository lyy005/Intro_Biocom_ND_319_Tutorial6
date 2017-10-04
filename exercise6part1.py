import os
import numpy
import pandas

#set the working directory
scores = pandas.read_csv("UWvMSU_1-22-13.txt", header=0, sep="\t")

#generate an array with a cumulative score for each team whenever either team scores 
A = numpy.zeros((51,3)) #tells python how big we want the table to be. 
B = pandas.DataFrame(A,columns=['time','UWscore','MSUscore']) #labels each column 

UWscore=0
MSUscore=0
for i in range(0,len(scores),1):
    if scores.iloc[i,1] == "UW":
        UWscore +=scores.iloc[i,2]
    else:
        MSUscore +=scores.iloc[i,2]
    B.iloc[i+1,1]=UWscore
    B.iloc[i+1,2]=MSUscore
    
    B.iloc[i+1,0]=scores.iloc[i,0]
    
import matplotlib.pyplot as plt
plt.plot(B.time,B.UWscore,'-r',B.time,B.MSUscore,'g-')
