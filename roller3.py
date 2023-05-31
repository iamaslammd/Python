print("Welcome to rollercoaster!")
height = int(input("What is your height? \n"))
bill = 0
if height >=120:
	print("You can ride")
	age = int(input("What is your age? \n "))
	if age<12 :
		bill = 5
		print("Child tickets are $5.")
	elif age<=18:
		bill = 7
		print("Youth ticket are $7.")
	else:
		bill = 12
		print("Adult ticket are $12.")
	photo = input("Do you want a photo taken? Y or N.")
	if photo == "Y":
		bill+=3
	print(f"Your final bill is ${bill}")	
else:
	print("Sorry, you have to grow taller to ride")