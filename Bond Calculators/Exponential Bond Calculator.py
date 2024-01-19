import numpy as np

def B_calculator_exp(P, C, r, y, f=1): # Bond Price
    
    B = P*np.exp(-r*y)+np.sum(C*P/f*np.exp(-r*(np.arange(1, y*f+1)/y)))
    return round(B, 2)

result = B_calculator_exp(100, 0.06, 0.0676, 2, 2) # Test
print(result)
