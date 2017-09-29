import random
guessesTaken=0
number= random.randint(1,100)
print('I am thinking of a number between 1 and 100')

while guessesTaken <10:
    print('Guess')
    guess= input()
    guess= int(guess)
    
    guessesTaken= guessesTaken + 1
    
    if guess < number:
        print ('Higher')
    if guess > number:
        print ('Lower')
    if guess == number:
        break
print('Correct!')