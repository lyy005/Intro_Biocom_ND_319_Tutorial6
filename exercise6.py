#### EXERCISE 6 #####

#question 1


#load the dataset
import pandas
import numpy
bball = pandas.read_csv("UWvMSU_1-22-13.txt", sep='\t', lineterminator='\r')
A=numpy.zeros((50,3))
B=pandas.DataFrame(A,columns=['Team','Time','CumeScore'])
for Team in bball:
    if Team= "MSU"



#question 2