def add_dots(string):
    sep = '.'
    x = sep.join(string)
    return x


def remove_dots(string):
    return string.replace(".", "")


#print(remove_dots(add_dots("hola")))
print(add_dots('hola'))
#print(remove_dots('h.o.l.a.'))