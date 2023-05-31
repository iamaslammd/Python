print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM?\n"))
if height>=120 :
	print("You can ride the rollercoaster!!")
	age = int(input("What is your age?\n"))
	if age<12:
		print("you have to pay $5")
	elif age<=18:
		print("you have to pay $7")
	else:
		print("You have to pay $12")
else:
	print("Sorry, you have to grow taller to ride")