#import prime_test as pt

def test_sum_squares(x):

    print(f'{x}:')
    square_numbers = []

    for i in range(1, int(x**(1/2))+1):
        square_numbers.append(i**2)

    print(square_numbers)
    #if pt.prime_test_func(x) == 1:
    
    for sq in square_numbers:
        y = x - sq
        print(y)
        if y in square_numbers:
            print(f'{x} = {y} + {sq}')
            square_numbers.remove(sq)

        else:
            pass
    #else:
    #    pass
test_sum_squares(30)