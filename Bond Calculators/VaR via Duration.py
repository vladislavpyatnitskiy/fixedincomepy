import numpy as np
from scipy.stats import norm

def VaR_D(P, C, r, y, f = 1, s = 1, VaR = 95): # Value-at-Risk for Bond
    
    B = P*(C/r * (1 - (1 + r/f) ** -(y*f)) + (1 + r/f) ** -(y*f)) # Bond Price

    PR = P * (1 + C / f) / (1 + r / f) ** (y * f)  # Principle Part
    PV = []
    payments = []
    
    for n in range(1, y * f):
        PV.append(C * P / f / (1 + r / f) ** (n * f))  # NPV
        payments.append(n * PV[n - 1])  # Coupon PV

    D = (sum(payments) + PR * y * f) / (PR + sum(PV))  # Duration
    
    return B * norm.ppf(1 - VaR*.01) * (D/(1 + (r - s*.01)/f)) * (r/f) # VaR

VaR_D(1000, 0.1, 0.05, 3, 1, 1) # Test
