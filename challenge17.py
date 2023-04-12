def all_equal(a):
    it = iter(a)
    b = next(it, None)
    return all(b == c for c in it)


print(all_equal([1,1,1]))