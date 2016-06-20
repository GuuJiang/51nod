n = int(input())
s = [int(input()) for i in range(n)]
s.insert(0, -1000000001)
f = [0] * (n + 1)

for i in range(1, n + 1):
    f[i] = max(f[j] for j in range(i) if s[j] < s[i]) + 1

print(max(f))
