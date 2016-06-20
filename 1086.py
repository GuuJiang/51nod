N, W = map(int, input().split())

items = []
for i in range(N):
    w, p, c = map(int, input().split())
    part = 1
    while c > part:
        items.append((w * part, p * part))
        c -= part
        part *= 2
    if c > 0:
        items.append((w * c, p * c))

f = [0] * (W + 1)
for item in items:
    for j in range(W, item[0] - 1, -1):
        f[j] = max(f[j], f[j - item[0]] + item[1])


print(f[-1])
