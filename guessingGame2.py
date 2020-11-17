import random
n = random.randint(1, 9)
chances=5
guess = input('Enter an integer from 1 to 9: ')
while chances>0:
    print
    if(guess < n):
        print('Guess is too low')
        guess = input('Enter an integer from 1 to 9: ')
        chances=chances-1
    elif(guess > n):
        print('Guess is too high')
        guess = input('Enter an integer from 1 to 9: ')
        chances=chances-1
    else:
        print('Congratulations You Won!')

if(chances==0):
    print('You lose, the number is' ,n)