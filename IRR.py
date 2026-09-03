import numpy as np
from scipy.optimize import root_scalar

def IRR(C, r, f=1):
    
    return root_scalar(
      lambda r: sum(C / (1 + r) ** np.arange(len(C))), 
      bracket=[0, 1], 
      args=(), 
      method='bisect'
      ).root * f
  
IRR(C=[-1000, 250, 300, 360, 432], r=.05)
