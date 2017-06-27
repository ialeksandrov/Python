for n in range(2, 11):
    print "n =", n

print "++++++++++++++++++++++++++++++++++++++++++"
print "While loop"

n = 2
while (n < 11):
    print "n =", n
    n = n + 1

print "==========================================="
print "doubles Functions"

def doubles(number):
    return number * 2

my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)
    print my_num
