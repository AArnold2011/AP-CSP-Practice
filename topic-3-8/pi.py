from decimal import Decimal, getcontext
import math

def chudnovsky_pi(digits):
    # Set the precision context to the requested number of digits + extra padding
    getcontext().prec = digits + 2
    
    # Define Chudnovsky constants
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = Decimal(L)
    
    # Calculate how many iterations are needed (approx 14 digits per iteration)
    iterations = math.ceil(digits / 14)
    
    for i in range(1, iterations + 1):
        # Update M_k iteratively based on the factorial logic
        # M_k = M_{k-1} * (k^3 - 16k) / i^3
        M = M * (K**3 - 16*K) // (i**3)
        L += 545140134
        X *= -262537412640768000
        
        S += Decimal(M * L) / X
        K += 12
    
    pi = C / S
    
    # Crop to requested digits
    getcontext().prec = digits
    return +pi

# Example: Compute 100 digits of Pi
print(chudnovsky_pi(10000))