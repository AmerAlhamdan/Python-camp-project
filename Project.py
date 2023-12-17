import time


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return (num1 / num2)
    except Exception as e:
        return e

def factorial_recursive(num1):
    if num1 < 0:
        return -1
    elif num1 == 0:
        return 1
    else:
        return num1 * factorial_recursive(num1 - 1)

def fibonacci(num1):
    if num1 <= 1:
        return num1
    else:
        return fibonacci(num1 - 1) + fibonacci(num1 - 2)

def switch_case(case):
    if case == 1:
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        return 'The addition of ' + str(num1) + ' and ' + str(num2) + ' is: ' + str(add(num1, num2))
    elif case == 2:
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        return 'The subtraction of ' + str(num1) + ' and ' + str(num2) + ' is: ' + str(sub(num1, num2))
    elif case == 3:
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        return 'The multiplication of ' + str(num1) + ' and ' + str(num2) + ' is: ' + str(multi(num1, num2))
    elif case == 4:
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        return 'The division of ' + str(num1) + ' and ' + str(num2) + ' is: ' + str(divide(num1, num2))
    elif case == 5:
        num1 = float(input('Enter your number: '))
        return 'The factorial of ' + str(num1) + ' is: ' + str(factorial_recursive(num1))
    elif case == 6:
        num1 = float(input('Enter your number: '))
        return 'The fibonacci of ' + str(num1) + ' is: ' + str(fibonacci(num1))
    else:
        return 'Invalid choice!'

def main():
    print('\n\n1- Add\n2- Subtract\n3- Multiply\n4- Divide\n5- Factorial\n6- Fibonacci')
    choice = int(input("Enter your mathematical operation: "))
    result = switch_case(choice)
    print(result)

if __name__ == "__main__":
    
    for i in range(5):
        
        main()
        
        time.sleep(3)
