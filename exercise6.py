#### EXERCISE 6 #####
#question 1

#load the dataset
import pandas
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
        bball2.loc[msu_list[i], "totalscore"] = bball2.totalscore.loc[msu_list[i - 1]] + bball2.score.loc[msu_list[i]]

print (bball2)

#making the plot!
from plotnine import *
p=(ggplot(data=bball2)
   + aes(x= "time", y= "totalscore", group= 'team', color= 'team')
   + geom_line()
   + geom_point()
   + xlab("Game Progress")
   + ylab("Total Score")
   + xlim(0,40)
   +scale_color_manual(values=['green','red'])
   + theme_classic()
)
print p


#question 2
import numpy
rand = numpy.random.randint(1, 101)  #Generates a random number
while True:   #Loops through three conditions
    print("I'm thinking of a number 1-100...")
    guess = input("Guess")  #Allows user to input a "Guess"
    if guess < rand:        #Returns appropriate hint for comparison of rand to Guess
        print("Higher")
        continue
    elif guess > rand:
        print("Lower")
        continue
    elif guess == rand:
        print("Correct!")
        break