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


num1 = int(input("What's the first number?\n"))
num2 = int(input("What's the second number?\n"))

for operation in operations:
    print(operation)

chose_operation = input("Pick an operation from the line above\n")

calculate_function = operations[chose_operation]
answer = calculate_function(num1, num2)

print(f"{num1} {chose_operation} {num2} = {answer}")
