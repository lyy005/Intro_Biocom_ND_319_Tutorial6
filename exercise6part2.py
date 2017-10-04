import numpy
import pandas
 
number=numpy.random.choice(range(1,100,1))
print "I'm thinking of a number between 1 and 100..."

Guess=0
while int(Guess) != number:
    Guess=raw_input("take a guess")
    if int(Guess)<number:
        print "Higher"
    elif int(Guess)>number:
        print "Lower"
    else:
        print "Correct"
