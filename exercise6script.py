import os
import numpy
import pandas

#set the working directory
scores = pandas.read_csv("UWvMSU_1-22-13.txt", header=0, sep=",")

#generate an array with a cumulative score for each team whenever either team scores 
A=numpy.zeros((51,3)) #tells python how big we want the table to be. 
B=pandas.DataFrame(A,columns=['time','Wisconsin','Michigan']) #labels each column 

UWscore=0
MSUscore=0
for i in range(2,len(scores),1):
    if scores.iloc[i,1] == "UW":
        UWscore += A.iloc[i,1]
    else:
        MSUscore +=A.iloc[i,2]
print A
