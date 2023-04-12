def list_xor(n,list1,list2):
    a = n in list1
    b = n in list2
    if  a + b == 1:
        return True
    else:
        return False



print(list_xor(1,[1,2,3],[1,6,4,5]))