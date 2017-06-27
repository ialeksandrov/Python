def hi():
    return "hi ivan!"

def doSomethingBeforeHi(func):
    print(func())

doSomethingBeforeHi(hi)
