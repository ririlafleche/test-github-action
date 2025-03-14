def miller_rabin_test(n, base):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    x = pow(base, d, n)
    if x == 1 or x == n - 1:
        return True
    
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    
    return False