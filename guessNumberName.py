import random
secretNumber=random.randint(1,20)
print('thinking a number between 1 and 20')

for guessesTaken in range(1,7):
    print('take a guess')
    guess=int(input())
    if guess<secretNumber:
        print('your guess is low')
        continue
    if guess>secretNumber:
        print('your guess is high')
    else:
        break
if guess==secretNumber:
    print('good!the number is '+str(guessesTaken)+' guesses')
else:
    print('no!the number is '+str(secretNumber))