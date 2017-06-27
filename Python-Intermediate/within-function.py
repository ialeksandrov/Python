def hi(name="ivan"):
    def greet():
        return "now you are in greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "ivan":
        return greet
    else:
        return welcome

a = hi()
print(a())
