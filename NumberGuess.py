#"Guess my Number" game
#Takes user input of a number from 1-100 and compares it to a randomly-generated value
#Tells user if their guess is higher or lower than the correct answer
#User may keep guessing until they get the correct value

import numpy
range=numpy.arange(1,101) #define array of possible number choices to exclude 0 and include 100
answer=numpy.random.choice(range) #generate a random number guess

print("I'm thinking of a number from 1-100. Take a guess!") #Initiate game
guess=input(prompt="Your guess:") #Store a guess from the user

while guess != answer: #Test if the user input is right
    if guess < answer: #If not, test whether the guess is lower or higher than the answer
        print(guess," is lower than my number.")
        guess=input(prompt="Guess again:")
    elif guess > answer:
        print(guess," is higher than my number.")
        guess=input(prompt="Guess again:")

print(guess," is the right answer!") #If the answer is correct, let the user know

