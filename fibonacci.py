def fibonacci(number):
    if number < 2: return number
    else: return fibonacci(number -1) + fibonacci(number - 2)

user_input = input("Enter a fibonacci number: ")
fib_user_input = fibonacci(user_input)
print fib_user_input
