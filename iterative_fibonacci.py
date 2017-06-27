def fibonacci(number):
    terms = [0, 1]
    i = 2
    while i <= number:
        terms.append(terms[i - 1] + terms[i -2])
        i = i + 1
    return terms[number]

user_input = input("Enter a fibonacci number: ")
fib_user_input = fibonacci(user_input)
print fib_user_input
