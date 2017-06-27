def accepts(*args):
    def check(func):
        


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

print(say_hello("Ivan"))
