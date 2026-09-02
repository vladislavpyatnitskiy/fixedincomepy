import numpy as np

def MIRR(C, r=0.1, I=1000):
  
    L = len(C)
  
    M = round((sum(C*((1+r)**(L - np.arange(1, L+1))))/I)**(1/L) - 1, 4)*100

    if M > r * 100:
        return f"MIRR is {M}% and more than cost of capital. Start project"
    
    return f"MIRR is {M}% and less than cost of capital. Don't start project"

MIRR(C = [300, 300, 300, 300], r = 0.12, I = 800)
