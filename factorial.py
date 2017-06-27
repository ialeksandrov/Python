def factorial(number):
    result = 1
    for i in range(number):
        result = result * (i + 1)

    return result

user_input = input("Enter a non-negative integer to take factorial of: ")
factorial_user_input = factorial(user_input)
print factorial_user_input
