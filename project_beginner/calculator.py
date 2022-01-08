def welcome():
    str1 = """
    Welcome to my calculator choose your favorite operator:
    [S] sum
    [R] resta
    [M] multiplication
    [D] Division
    """
    return print(str1)


def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


while True:
    welcome()
    enter = input("?")
    if enter.isalpha():
        a1 = enter.upper()
        number_1 = int(input("which is the first value: "))
        print("")
        number_2 = int(input("Which is the second value: "))

        if a1 == "S":
            print(number_1, "+", number_2, "=", add(number_1, number_2))

        elif a1 == "R":
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))

        elif a1 == "M":
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))

        elif a1 == "D":
            print(number_1, "/", number_2, "=", divide(number_1, number_2))
        else:
            print("Invalid input")

    else:
        break
