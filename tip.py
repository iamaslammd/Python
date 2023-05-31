print("Welcome to tip calculator")
bill = float(input("What was the total bill?\n $ "))
tip = int(input("What percentage tip would you like to give? 10,12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))
b= tip/100*bill+bill
final_bill = round(b/people,2)
print(f"Each person shold pay : $ {final_bill}")