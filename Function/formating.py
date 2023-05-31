#Funtion with output
def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input."
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"
print(format_name(input("First Name: "),input("Last Name: ")))
