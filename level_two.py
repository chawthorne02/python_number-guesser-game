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
        print(f"You lose. The computer guessed your number. Your number is {number}.")
        break
    elif computer_guess < number:
        print(f"The computer guessed too low. The computer guessed {computer_guess}.")
    elif computer_guess > number:
        print(f"The computer guessed too high. The computer guessed {computer_guess}.")

    if guesses == 3:
        print('The computer could not guess your number. You just beat the computer.')