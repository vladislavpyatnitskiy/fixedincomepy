def bond_calculator(P, C, r, f, y):

  B = P * (C / r * (1 - (1 + r / f) ** -(y * f)) + (1 + r / f) ** -(y * f))
  
  print(round(B, 2))
  
bond_calculator(1000, 0.1, 0.07, 1, 3)  
