import math

def calc_value(stock, u, d, r, t, strike):
    p = (math.exp(r * t) - d) / (u - d)
    f_uu = strike - stock * u**2
    f_uu = f_uu if f_uu > 0 else 0
    f_ud = strike - stock * u * d
    f_ud = f_ud if f_ud > 0 else 0
    f_dd = strike - stock * d**2
    f_dd = f_dd if f_dd > 0 else 0
    print(f_uu, f_ud, f_dd)
    return math.exp(-2 * r * t) * \
        (p**2 * f_uu + 2*p*(1-p)*f_ud + (1-p)**2*f_dd)
        
print(calc_value(40, 1.1, 0.9, 0.12, 0.5, 42))