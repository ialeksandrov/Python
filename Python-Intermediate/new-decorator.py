def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_funtion_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_funtion_requiring_decoration()