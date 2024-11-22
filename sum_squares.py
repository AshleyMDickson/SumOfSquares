a = input("Please enter your starting number: ")
b = input("Now enter your ending number: ")

def test_sum_squares(x):

    print(f'{x}:')
    square_numbers = []

    for i in range(1, int(x**(1/2))+1):
        square_numbers.append(i**2)
    
    for sq in square_numbers:
        y = x - sq

        if y in square_numbers:
            print(f'    = {y} + {sq}')
            square_numbers.remove(sq)

        else:
            pass

for _ in range(int(a), int(b)):
    test_sum_squares(int(_))
