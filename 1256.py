

def egcd(m, n):
    if n == 0:
        return (m, 0, 1)
    g, x, y = egcd(n, m % n)
    return (g, y - (m // n) * x, x)

m, n = map(int, input().split())
g, x, y = egcd(m, n)
assert g == 1
print(y if y > 0 else n + y)
