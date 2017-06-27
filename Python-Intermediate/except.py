try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occured. {}'.format(e.args[-1]))
finally:
    print("This would be printed wether or not an exception occured!")
