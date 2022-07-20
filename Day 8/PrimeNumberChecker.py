# Create a function that check whether or not an input number is a prime number.

def prime_checker(number):

    for i in range(2, number):
        if number % i == 0:
            print("It is not a prime number")
        else:
            print("It is a prime number")


