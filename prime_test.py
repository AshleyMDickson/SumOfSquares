def prime_test_func(x):
    
    factors = []
    
    for i in range(2, int(x/2)):
        
        if x%i == 0:
            
            factors.append(i)
            
    y = len(factors)
    
    if y==0:
        print("x is prime")
    else:
        print("nope")