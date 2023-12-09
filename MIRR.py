def MIRR(C, r=0.1, I=1000):
    mirr_value = round((sum(C * ((1 + r) ** (len(C) - np.arange(1, len(C) + 1)))) / I) ** (1 / len(C)) - 1, 4) * 100

    if mirr_value > r:
        return f"MIRR is {mirr_value}% > cost of capital. Start project"
    else:
        return f"MIRR is {mirr_value}% < cost of capital. Don't start"

MIRR(C = [300, 300, 300, 300], r = 0.12, I = 800)
