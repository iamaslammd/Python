from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5
# Function to check user's guess against actual answer
def check_guess(users_choice, chosen_number):
    if users_choice > chosen_number:
        return("Too High!!")
    elif users_choice < chosen_number:
        return("Too Low!!")
    else:
        print(f"You got it! The answer is {chosen_number}")

# Function for dificulty level
def dificulty_level():
    level = input("Choose a dificulty levl. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL   

# from guessNumberArt import logo
# print(logo)
print("Welcome to number gussing game.")
print("I'm gussing a number between 1 and 100")
chosen_number = randint(1, 100)
print(f"The correct answer is {chosen_number}") 

# Let the user guess the number
attempts = dificulty_level()
print(f"You have {attempts} attempts remaining to guess the number.")
users_choice = int(input("Make a guess!!"))
check_guess(users_choice, chosen_number)
