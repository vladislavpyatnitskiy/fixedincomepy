def NPV(C, r):
    return sum(C / (1 + r) ** np.arange(len(C)))

NPV(C=[-1000, 250, 300, 360, 432], r=0.05) # Test
