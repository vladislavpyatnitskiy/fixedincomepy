from scipy.optimize import root_scalar

def IRR(C, r):
    equation = lambda r: sum(C / (1 + r) ** np.arange(len(C)))
    result = root_scalar(equation, bracket=[0, 1], args=(), method='bisect')
    return result.root
  
IRR(C=[-1000, 250, 300, 360, 432], r=.05)
