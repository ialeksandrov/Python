def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

user_input = input("Enter a non-negative integer to take factorial of: ")
factorial_user_input = factorial(user_input)
print factorial_user_input
