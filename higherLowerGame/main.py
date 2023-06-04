from data import data
from art import logo,vs
import random

def format_data(account):
    """Formating the account data """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name},a {account_descr}, from {account_country}")

def check_ans(user_input,a_follower,b_follower):
    """ Using if statement to check the users answer """
    if a_follower > b_follower:
        return user_input == "a"
    else:
        return user_input == "b" 
# # Display a ascii art
print(logo)
score =0
continue_game = True
account_b = random.choice(data)
# Make a game repeatable.
while continue_game:
    # # Generate a random insta account from the data

    # # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b: 
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Asking the user to guess the answer
    user_input =  input("Who has more instagram follower's? Type 'A' or 'B': ").lower()

    # Check if user is correct or not

    ## Git followers count of each account
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_ans(user_input,a_followers_count,b_followers_count)
    # Give user feedback over their guess
    #Score keeping
    if is_correct:
        score += 1
        print(f"You're right!! Current Score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final Score: {score}")

