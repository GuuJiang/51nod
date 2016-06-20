n, w = map(int, input().split())
items = [tuple(map(int, input().split())) for i in range(n)]

f = [0] * (w + 1)
for item in items:
    for j in range(w, item[0] - 1, -1):
        f[j] = max(f[j], f[j - item[0]] + item[1])


print(f[w])
