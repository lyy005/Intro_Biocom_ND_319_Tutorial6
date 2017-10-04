#### EXERCISE 6 #####

#question 1









#question 2
import numpy
rand = numpy.random.randint(1, 101)
while True:
    print("I'm thinking of a number 1-100...")
    guess = input("Guess")
    if guess < rand:
        print("Higher")
        continue
    elif guess > rand:
        print("Lower")
        continue
    elif guess == rand:
        print("Correct!")
        break

