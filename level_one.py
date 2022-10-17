# LEVEL ONE

# In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.

from random import randint

def play():
    guess_taken = 0

    number = randint(1, 10)
    player = print('I am thinking of a number 1 through 10. ')

    while guess_taken < 3:
        print(f'You have {3-guess_taken} tries to guess the correct number')
        guess = input()
        guess = int(guess)

        guess_taken = guess_taken + 1

        if guess < number:
            print('Your guess is too low')

        elif guess > number:
            print('Your guess is too high.')

        elif guess == number:
            print('Great Job! You guessed the correct number!')
            break

        if guess_taken == 3:
            number = str(number)
            print('You ran out go guesses! The number I was thinking of is ' + number)


if __name__ == '__main__':
    play()
