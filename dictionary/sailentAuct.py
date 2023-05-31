def clear():
    print('\n'*90)

from auctArt import logo
print(logo)

bids ={}
finsihed = False

def hightest_bidder(bidding_record):
    hightest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > hightest_bid:
            hightest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid ${hightest_bid}")
    

while not finsihed:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $ "))
    bids[name] = price
    should_continue = input("Are there any other bids? Type 'yes' or 'no'")
    if should_continue == "no":
        finsihed = True
        hightest_bidder(bids)
    elif should_continue == "yes":
        clear()




