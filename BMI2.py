height = float(input("Enter your height in M: "))
weight = float(input("Enter your wieght in KG : "))
bmi = round(weight/height**2,2)
if bmi<18.5:
	print(f"Your BMI is {bmi}.You are Underweight")
elif bmi<25:
	print(f"Your BMI is {bmi}.You have a normal weight")
elif bmi<30:
	print(f"Your BMI is {bmi}.You are over weight")
elif bmi<35:
	print(f"Your BMI is {bmi}.You are obese")
else:
	print(f"Your BMI is {bmi}.You are clinically obese")
