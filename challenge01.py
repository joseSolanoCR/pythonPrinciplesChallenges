def capital_indexes(string):
    capitals = []
    for a in range(len(string)):
        if string[a].isupper():
            capitals.append(a)
    return capitals

def mid(string):
    if len(string) % 2 ==0:
        return ''
    else:
        print(round((len(string)/2),0))
        return string[round(len(string)/2)-1]
print (mid("abc"))