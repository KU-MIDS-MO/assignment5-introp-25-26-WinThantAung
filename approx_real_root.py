def approx_real_root(coeffs, interval):
    a0, a1, a2, a3 = coeffs
    a, b = interval

    def p(x):            #polynomial
        return a0 + a1*x + a2*x**2 + a3*x**3

    tolerance = 1e-9       # bisection

    while (b - a) / 2 > tolerance:
        m = (a + b) / 2

        if p(a) * p(m) <= 0:
            b = m
        else:
            a = m

    return (a + b) / 2

