m, n = map(int, input().split())

M = [list(map(int, input().split())) for i in range(n)]
c = [0] * m

result = 0
for i in range(n):
    for j in range(i, n):
        s = 0
        for k in range(m):
            c[k] = M[j][k] if i == j else c[k] + M[j][k]
            s = c[k] if s < 0 else s + c[k]
            result = max(result, s)

print(result)
