import numpy as np
numbers=np.arange(100)+1
answer=np.random.choice(numbers)
guess=0
name= raw_input ("What is your name?")
print("Wanna play a game %s?") %(name)
print("Guess a number 1-100")
while guess!= answer:
    guess = input ("Your guess is:")
    if guess > 0:
        if guess > answer:
            print "Lower"
        else:
            print "Higher"
    else:
        break
else:
    print ("Congrats %s, you win....this time") %(name)











