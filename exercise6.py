#### EXERCISE 6 #####

#question 1


#load the dataset
import pandas
bball = pandas.read_csv("UWvMSU_1-22-13.txt", sep='\t', lineterminator='\r')

#create blank column totalscore
bball2=bball.assign(totalscore="")
print bball2







#question 2