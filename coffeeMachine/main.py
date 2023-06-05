MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 20,
    }
}

earning = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient_resources(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("How many ₹5 coins: ")) * 5
    total += int(input("How many ₹10 coins: ")) * 10
    total += int(input("How many ₹20 coins: ")) * 20
    return total

def is_transaction_sucessful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ₹{change} in change")
        global earning
        earning += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded. ")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!!")

coffe_on = True
while coffe_on:
    Choice = input("What would like to have? Espresso Latte Cappuccino: ").lower()
    if Choice == "off":
        coffe_on = False
    elif Choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}G")
        print(f"money: ₹{earning}")
    else:
        order = MENU[Choice]
        if sufficient_resources(order["ingredients"]):
            payment = process_coin()
            if is_transaction_sucessful(payment,order["cost"]):
                make_coffee(Choice,order["ingredients"])

