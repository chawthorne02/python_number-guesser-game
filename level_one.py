# LEVEL ONE

# In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.

from random import randint

guess_taken = 0

number = randint(1, 10)
player = print('I am thinking of a number 1 through 10. ')

while guess_taken < 3:
    print('You have 3 tries to guess the correct number')
    guess = input()
    guess = int(guess)

    guess_taken = guess_taken + 1

    if guess < number:
        print('Your guess is too low')

    elif guess > number:
        print('Your guess is too high.')

    elif guess == number:
        break

    elif guess == number:
        print('Great Job! You guessed the correct number!')

    else guess !== number:
        number = str(number)
        print('Wrong! The number I was thinking of is ' + number)


