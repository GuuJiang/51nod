n, p = map(int, input().split())

result = 1
for i in range(2, n + 1):
    result = result * i % p
    if result == 0:
        break

print(result)
