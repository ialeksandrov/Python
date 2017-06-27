import math


def message_to_numbers(messsage):
    dict = {2:"a", 22:"b", 222:"c", 3:"d", 33:"e" , 333:"f" , 4:"g" , 44:"h", 444:"i" , 5:"j", 55:"k", 555:"l", 6:"m", 66:"n", 666:"o", 7:"p", 77:"q", 777:"r", 7777:"s", 8:"t", 88:"u", 888:"v", 9:"w", 99:"x", 999:"y", 9999:"z"}
    new_dict = {}
    result = []
    last_new_dict_item = 0

    for key, value in dict.items():
        # print (key, value)
        new_dict[value] = key

    for item in messsage:
        if item == " ":
            result.append(0)
        else:
            if item.isupper():
                result.append(1)
                item = item.lower()
            new_dict_item = new_dict[item]
            new_dict_item = new_dict_item % 10
            if last_new_dict_item == new_dict_item:
                result.append(-1)
            last_new_dict_item = new_dict_item
            string_item = str(new_dict[item])
            for str_item in string_item:
                result.append(int(str_item))
    # print ( result )
    return result

print(message_to_numbers("abc"))
print(message_to_numbers("a"))
print(message_to_numbers("Ivo e Panda"))
print(message_to_numbers("aabbcc"))
