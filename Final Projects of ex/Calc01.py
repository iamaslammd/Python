from calcArt import logo
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print(logo)
    num1 = float(input("First number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("Next Number: "))
        calculation_fun = operations[operation_symbol]
        answer = calculation_fun(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()