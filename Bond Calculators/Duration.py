def duration(P, C, r, y, f=1, s=1):
    
    P_ = P * (1 + C / f) / (1 + r / f) ** (y * f)  # Principle Part
    PV = []
    payments = []
    
    for n in range(1, y * f):
        PV.append(C * P / f / (1 + r / f) ** (n * f))  # NPV
        payments.append(n * PV[n - 1])  # Coupon PV

    D = (sum(payments) + P_ * y * f) / (P_ + sum(PV))  # Duration

    # Table with Duration and Modified Duration
    bond_list = [
        round(D, 3),
        round(D / (1 + (r - s * 0.01) / f), 2)
    ]

    return bond_list # Display sentence

duration(1000, 0.1, 0.05, 3, 1, 1) # Test
