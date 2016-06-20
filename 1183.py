a = input()
b = input()
la = len(a) + 1
lb = len(b) + 1

f = [i for i in range(lb)]
for i in range(1, la):
    last = f[0]
    f[0] = i
    for j in range(1, lb):
        t = f[j]
        f[j] = min(last + (a[i - 1] != b[j - 1]), t + 1, f[j - 1] + 1)
        last = t
print(f[lb - 1])
