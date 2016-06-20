s = sorted(input())
n = len(s)
while True:
    print(''.join(s))
    for i in range(n - 1, 0, -1):
        if s[i - 1] < s[i]:
            break
    else:
        break
    mj = i
    for j in range(i, n):
        if s[j] > s[i - 1] and s[j] < s[mj]:
            mj = j
    s[i - 1], s[mj] = s[mj], s[i - 1]
    s[i:n] = sorted(s[i:n])
