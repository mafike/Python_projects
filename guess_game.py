# Guessing Game In this project, we will create a program in which the system will choose a random number between any
# ranges defined, and then the user is given a hint to guess the number. Every time the user guesses the number
# wrongly, he is given another clue leading him toward the answer. The clue can be of any type like smaller, greater,
# multiples, dividers, etc.
# We will also need a function for checking whether the input is correct or not and to check the difference between
# the original number and the number guessed.
import random
number = random.randint(1, 10)
player_name = input("Hello, what's your name? ")
number_of_guesses = 0
print(f"Okay! {player_name} I am guessing a number between")
while number_of_guesses < 5:
    guess = int(input('> '))
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    elif guess == number:
        break
if guess == number:
    print(f"You guessed the right number in {str(number_of_guesses)} tries! ")

else:
    print(f"You did not guess the number, the number was {str(number)}")