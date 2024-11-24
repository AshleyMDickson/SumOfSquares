#a = int(input("Enter a number for prime testing: "))

def prime_test_func(x):
    
    factors = []
    
    for i in range(2, int(x**(1/2))+1):
        if x%i == 0:
            factors.append(i)
            
    y = len(factors)
    
    if y==0:
        #print(f'{x} is prime.')
        return 1;
    else:
        #print(f'{x} is composite.')
        return 0;

#prime_test_func(a)
