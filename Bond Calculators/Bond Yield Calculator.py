from scipy.optimize import root_scalar

def yield_calculation(C, r):
    equation = lambda r: sum(C / (1 + r) ** np.arange(len(C)))
    result = root_scalar(equation, bracket=[0, 1], args=(), method='bisect')
    return result.root * 2
  
yield_calculation(C=[-98.39, 3, 3, 3, 103], r=0.05)
