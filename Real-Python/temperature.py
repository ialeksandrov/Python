def Farenheit(Celsius):
    far_temp = Celsius * 9 / 5 + 32
    return far_temp

def Celsius(Farenheit):
    cel_temp = (Farenheit - 32) * 5 / 9
    return cel_temp

temp1 = 72
print("{} degrees F = {} degrees C".format(temp1, Celsius(temp1)))

temp2 = 37
print("{} degrees C = {} degrees F".format(temp2, Farenheit(temp2)))
