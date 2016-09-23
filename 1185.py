import decimal

g = (decimal.Decimal('5').sqrt() + 1) / 2

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print('B' if min(a, b) == int(abs(a - b) * g) else 'A')