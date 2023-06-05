from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5
# Function to check user's guess against actual answer
def check_guess(users_choice, chosen_number,attempts):
    if users_choice > chosen_number:
        print("Too High!!")
        return attempts -1
    elif users_choice < chosen_number:
        print("Too Low!!")
        return attempts -1
    else:
        print(f"You got it! The answer is {chosen_number}")

# Function for dificulty level
def dificulty_level():
    level = input("Choose a dificulty levl. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL   

def game():
    from guessNumberArt import logo
    print(logo)
    print("Welcome to number gussing game.")
    print("I'm gussing a number between 1 and 100")
    chosen_number = randint(1, 100)
    print(f"The correct answer is {chosen_number}")
    attempts = dificulty_level()
    users_choice = 0
    while users_choice != chosen_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        # Let the user guess the number
        users_choice = int(input("Make a guess: "))
        attempts =  check_guess(users_choice, chosen_number,attempts)
        if attempts == 0:
            print("You ran out of attempts. You lose")
            return
        elif users_choice != chosen_number:
            print("Guess Again.")
game()