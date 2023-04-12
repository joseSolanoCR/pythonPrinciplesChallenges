a = [1,2,3,4]
b = [5,6,7,8]

def zap(a,b):
    list = []
    for x in range(len(a)):
        list.append((a[x],b[x]))
    return list

print(zap(a,b))