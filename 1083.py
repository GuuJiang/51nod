n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

dp = [0] * (n + 1)
for i in range(n):
    for j in range(1, n + 1):
        dp[j] = max(dp[j], dp[j - 1]) + a[i][j - 1]

print(dp[n])
