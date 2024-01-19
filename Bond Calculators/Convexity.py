def convexity(P, C = 0, r = 0, y = 0, f = 1, s = 1):
    
    l = [] # List for all price values

    # Calculate all 3 prices; Product of maturity and repayment number
    for n in range(-1, 2, 1):
        d = (1 + (r + s * n / 100) / f) ** -y * f

        # Calculate price of bond and add result to list
        l.append(P * (C / (r + s * n / 100) * (1 - d) + d))

    # Convexity
    result = round((l[0] + l[2] - 2 * l[1]) / l[1] / (s / 100) ** 2,2)
    return result

convexity_result = convexity(P=1000, C=0.1, r=0.05, y=3, f=1, s=1) # Test
print(convexity_result)
