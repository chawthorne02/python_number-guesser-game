#LEVEL TWO

# In level two, the game is reversed and the user picks a number and the computer then has 3 guesses to select the correct answer.


from random import randint

prompt= input('Alright computer you have three tries to guess the number')
number = int(prompt)

guesses = 0

while guesses < 3:
    computer_guess = randint(1, 10)
    print("The Computer guesses", computer_guess)

    guesses = guesses + 1

    if computer_guess == number:
        break
    elif computer_guess < number:
        print("Your number is too low buddy")
    elif computer_guess > number:
        print('Your number is too high pal')

if computer_guess == number:
    print("Wow! The computer has guessed your number!")
elif computer_guess != number:
    print('The computer could not guess my number. I just beat the computer.')