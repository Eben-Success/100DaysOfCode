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
num2 = int(input("What's the second number?\n"))


def operation():
    for symbol in operations:
        print(symbol)


operation()

chose_operation = input("Pick an operation from the list above\n")

calculate_function = operations[chose_operation]

answer = calculate_function(num1, num2)

print(f"{num1} {chose_operation} {num2} = {answer}")

num3 = int(input("\nWhat's the third number"))
operation()

chose_operation = input("Pick an operation from the list above\n")
final_answer = calculate_function(answer, num3)

print(f"{answer} {chose_operation} {num3} = {final_answer}")
