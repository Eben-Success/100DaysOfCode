# Creating a calculator from scratch

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number? \n"))
for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:
    symbol = input("Pick an operations:\n")
    num2 = int(input("What's the next number:\n"))
    calculation_function = operations[symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {symbol} {num2} = {first_answer}")
