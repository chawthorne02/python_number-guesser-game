# LEVEL FOUR


# In level four, give the user an option to play against the computer or to think of a number for the computer to guess.

from level_one import play
from level_three import computer_guess

print("Let's Play a Game!")
choice = input(
    "Hit 'a' for me to choose a number for you to guess, hit 'b' to choose a number for me to guess! "
)

if choice.lower() == "a":
    play()
elif choice.lower() == "b":
    computer_guess()