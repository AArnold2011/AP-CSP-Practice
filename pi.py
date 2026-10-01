from decimal import Decimal, getcontext
import math

def chudnovsky_pi(digits):
    getcontext().prec = digits + 2
    

    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = Decimal(L)
    
    iterations = math.ceil(digits / 14)
    
    for i in range(1, iterations + 1):
        M = M * (K**3 - 16*K) // (i**3)
        L += 545140134
        X *= -262537412640768000
        
        S += Decimal(M * L) / X
        K += 12
    
    pi = C / S
    
    getcontext().prec = digits
    return +pi

print(chudnovsky_pi(10000))