import numpy as np
from scipy.stats import norm

def VaR_D(P, C, r, y, f = 1, s = 1, VaR = 95):
    
    B = P*(C/r * (1 - (1 + r/f) ** -(y*f)) + (1 + r/f) ** -(y*f)) # Bond Price

    P_ = P * (1 + C / f) / (1 + r / f) ** (y * f)  # Principle Part
    PV = []
    payments = []
    
    for n in range(1, y * f):
        PV.append(C * P / f / (1 + r / f) ** (n * f))  # NPV
        payments.append(n * PV[n - 1])  # Coupon PV

    D = (sum(payments) + P_ * y * f) / (P_ + sum(PV))  # Duration
    
    var_result = B * norm.ppf(1 - VaR*.01)*(D/(1 + (r - s*.01)/f))*(r/f) # VaR
    return var_result

var_result = VaR_D(1000, 0.1, 0.05, 3, 1, 1) # Test
print(var_result)
