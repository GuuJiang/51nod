n = int(input())
numbers = [int(input()) for i in range(n)]

s = sum(numbers)
w = (s + 1) // 2

f = [0] * (w + 1)
for i in numbers:
    for j in range(w, i - 1, -1):
        f[j] = max(f[j], f[j - i] + i)

print(abs(f[w] * 2 - s))
