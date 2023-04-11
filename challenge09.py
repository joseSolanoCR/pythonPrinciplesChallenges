def is_anagram(a, b):
    al = list(a)
    bl = list(b)
    al.sort()
    bl.sort()
    return al == bl

print(is_anagram("hola","loha"))