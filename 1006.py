a = input()
b = input()
la = len(a) + 1
lb = len(b) + 1

lcs = [[0] * lb for i in range(la)]
path = [[0] * lb for i in range(la)]

for i in range(1, la):
    for j in range(1, lb):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            path[i][j] = 3
        elif lcs[i][j - 1] > lcs[i - 1][j]:
            lcs[i][j] = lcs[i][j - 1]
            path[i][j] = 2
        else:
            lcs[i][j] = lcs[i - 1][j]
            path[i][j] = 1

result = ''
i, j = la - 1, lb - 1
while i > 0 and j > 0:
    d = path[i][j]
    if d == 1:
        i -= 1
    elif d == 2:
        j -= 1
    else:
        assert(a[i - 1] == b[j - 1])
        result += a[i - 1]
        i -= 1
        j -= 1

print(result[::-1])
