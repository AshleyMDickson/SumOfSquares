#a = int(input("Enter a number of prime testing: "))

def prime_test_func(x):
    
    factors = []
    
    for i in range(2, int(x**(1/2))):
        
        if x%i == 0:
            
            factors.append(i)
            
    y = len(factors)
    
    if y==0:
        return 1;
        #print(f'{x} is prime.')
    else:
        return 0;
        #print(f'{x} is composite.')

#prime_test_func(a)
