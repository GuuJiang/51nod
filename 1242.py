def mat_multi(m1, m2):
    return ((m1[0] * m2[0] + m1[1] * m2[2]) % 1000000009,
        (m1[0] * m2[1] + m1[1] * m2[3]) % 1000000009,
        (m1[2] * m2[0] + m1[3] * m2[2]) % 1000000009,
        (m1[2] * m2[1] + m1[3] * m2[3]) % 1000000009)

def mat_pow(m, n):
    result = (1, 0, 0, 1)
    while n:
        if n & 1:
            result = mat_multi(result, m)
        m = mat_multi(m, m)
        n >>= 1
    return result

def fib(n):
    m = mat_pow((1, 1, 1, 0), n)
    return m[1] % 1000000009
    

print(fib(int(input())))