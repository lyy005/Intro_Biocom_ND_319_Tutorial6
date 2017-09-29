#"Guess my Number" game
#Takes user input of a number from 1-100 and compares it to a randomly-generated value
#Tells user if their guess is higher or lower than the correct answer
#User may keep guessing until they get the correct value

import numpy
range=numpy.arange(1,101) #define array of possible number choices to exclude 0 and include 100
answer=numpy.random.choice(range) #generate a random number guess

