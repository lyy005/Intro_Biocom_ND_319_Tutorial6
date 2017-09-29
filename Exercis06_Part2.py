import random
guessesTaken=0
number= random.randint(1,100)
print('I am thinking of a number between 1 and 100')
while guessesTaken <6:
    print('Make a guess')
    guess= input()
    guess= int(guess)
    
    guessesTaken= guessesTaken + 1
    
    if guess < number:
        print ('Too low')
    if guess > number:
        print ('Too high')
    if guess == number:
        print('Good job!')
