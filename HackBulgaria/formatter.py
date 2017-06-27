def formatter(str_to_format, **kwargs):
    placeholder_string = "{{#}}"
    start = ""
    end = ""

    if 'placeholder' in kwargs.keys():
        placeholder_string = kwargs["placeholder"]

    index = placeholder_string.find('#')
    if index is not -1:
        start = placeholder_string[:index]
        end = placeholder_string[index + 1:]

    for name, value in kwargs.items():
        if name is not "placeholder" and index is not -1:
            str_to_replace = start + name + end
            str_to_format = str_to_format.replace(str_to_replace, value)
    return str_to_format

print(formatter('Hello, I am {{name}}!', name='Rado'))
print(formatter('Hello, I am {name}!', placeholder='{#}', name='Rado'))
print(formatter('Hello, I am [name]!', placeholder='[#]',  name='Rado'))
