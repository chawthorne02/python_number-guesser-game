# LEVEL THREE


# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes computer before it correctly guesses the number.

# Floored quotient // 2
# Mady's version
def computer_guess():
    number = int(input("Enter a number between 1 and 100: "))
    if number < 1 or number > 100:
        print("Must be a number between 1 and 100.")
        computer_guess()
    else:
        guessesTaken = 1
        low = 1
        high = 100
        guess = (low+high)//2

        while guess != number:
            guessesTaken = guessesTaken + 1
            if guess > number:
                high = guess
                print("The computer takes a guess...", guess, "is too high.")
            elif guess < number:
                low = guess + 1
                print("The computer takes a guess...", guess, "is too low.")
            guess = (low+high)//2
            
        print(f"The computer guessed your number in {guessesTaken}. It was {guess}.")


if __name__ == '__main__':
    computer_guess()

