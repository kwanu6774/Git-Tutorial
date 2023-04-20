def display_multiplication_table():
    for n in range(1,10):
        for i in range(2,6):
            print(f'{i} x {n} = {n*i:2}',end='\t')
        print('')
    print('')
    for n in range(1,10):
        for i in range(6,10):
            print(f'{i} x {n} = {n*i:2}',end='\t')
        print('')



display_multiplication_table()

