import math

def group(items):
    if len(items) == 0:
        return []
    grouped_items = []
    prev_item, rest_items = items[0], items[1:]


    subgroup = [prev_item]
    for item in rest_items:
        if item != prev_item:
            grouped_items.append(subgroup)
            subgroup = []
        subgroup.append(item)
        prev_item = item
    grouped_items.append(subgroup)
    return grouped_items

def to_number(list_of_digits):
    result = 0
    for digit in list_of_digits:
        result = result * 10 + int(digit)
    return result


def numbers_to_message(pressed_sequence):
    result = ""
    upper = False
    new_list = group(pressed_sequence)
    dict = {2:"a", 22:"b", 222:"c", 3:"d", 33:"e" , 333:"f" , 4:"g" , 44:"h", 444:"i" , 5:"j", 55:"k", 555:"l", 6:"m", 66:"n", 666:"o",
        7:"p", 77:"q", 777:"r", 7777:"s", 8:"t", 88:"u", 888:"v", 9:"w", 99:"x", 999:"y", 9999:"z"}
    for item in new_list:
        if item == [1]:
            upper = True
        elif item != [-1] and item != [0] and item != [1]:
            number_for_decode = to_number(item)
            if len(item) > 3:
                if number_for_decode % 10 in [2, 3, 4, 5, 6, 8]:
                    alpha = dict[math.floor(number_for_decode / 1000)]
                else:
                    alpha = dict[math.floor(number_for_decode / 10000)]
            else:
                alpha = dict[number_for_decode]
            if (upper == True):
                alpha = alpha.upper()
                upper = False
            result = result + str(alpha)
        elif item == [0]:
            result = result + " "

    return result

print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
