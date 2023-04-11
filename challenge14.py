def palindrome(a):
    normal = list(a)
    reversed = []
    for i in range(len(a) - 1, -1, -1):
        reversed.append(a[i])

    return normal == reversed


print(palindrome('bob'))
