from scipy.optimize import root_scalar
import numpy as np

def yield_calculation(C, r, f=1):
    equation = lambda r: sum(C / (1 + r) ** np.arange(len(C)))
    result = root_scalar(equation, bracket=[0, 1], args=(), method='bisect')
    return round(result.root * f, 4)
  
yield_calculation(C=[-98.39, 3, 3, 3, 103], r=0.05, f=2)
