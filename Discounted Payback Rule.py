def DPR(C, r, I, DP=0, period=0):
    n = 0

    # When Payback Sum < Initial Value add Cash Flow for each year
    while DP <= I:
        for cash_flow in C:
            n += 1
            DP += cash_flow / (1 + r) ** n

            # When Payback Sum > Initial Value, calculate Payback Period
            if DP > I:
                period = (I - DP) / (cash_flow / (1 + r) ** n) + n
                break

    return f"Payback period is {round(period, 2)} years"
  
DPR(C = [100, 100, 100, 100], r = 0.1, I = 200)
