def get_row_col(a):
    x =''
    y = ''
    if a[0] == 'A':
        x = 0
    elif a[0] =='B':
        x = 1
    elif a[0] == 'C':
        x = 2
    if a[1] == '1':
        y = 0
    elif a[1] =='2':
        y = 1
    elif a[1] == '3':
        y = 2

    return (y,x)


print(get_row_col('A3'))