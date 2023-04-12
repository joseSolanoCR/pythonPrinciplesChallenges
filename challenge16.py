def consecutive_zeros(a):
    lista = a.split('1')
    lista.sort(reverse=True)
    return len(lista[0])



print(consecutive_zeros('100110001110000'))