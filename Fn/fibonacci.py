def f(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    
    a, b = 0, 1
    # Zaczynamy od i=3, ponieważ n=1 i n=2 są już obsłużone
    for _ in range(3, n + 1):
        a, b = b, a + b
        
    return b