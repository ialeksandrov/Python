from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_funtion_requiring_decoration():
    """Hey yo! Decorate me !"""
    print("I am the function which needs some decoration to remove the foul smell")

print(a_funtion_requiring_decoration.__name__)
