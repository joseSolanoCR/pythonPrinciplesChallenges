def double_letters(string):
    b = ''
    for a in string:

        if a == b:
            return True
        else:
            b=a
    return False

print(double_letters('holla'))