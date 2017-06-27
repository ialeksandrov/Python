def hack_dict(list=None, **kwargs):
    if list:
        return {item[0]: item[1] for item in list}
    else:
        return {name: value for name, value in kwargs.items()}

print(hack_dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print(hack_dict(sape=4139, guido=4127, jack=4098))
