import numpy

randomNumber = numpy.random.choice(numpy.arange(1,101))
Guess = -1
print("I'm thikning of a number 1-100...")
while Guess != randomNumber:
    Guess = input("Guess: ")
    if Guess > randomNumber:
        print("Lower")
    if Guess < randomNumber:
        print("Higher")
print("Correct!")