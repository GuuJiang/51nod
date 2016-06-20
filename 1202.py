N = int(input())
a = [int(input()) for i in range(N)]
pos = [0] * 100001
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    dp[i] = dp[i - 1] * 2
    p = pos[a[i - 1]]
    if p > 0:
        dp[i] -= dp[p - 1]
    dp[i] %= 1000000007
    pos[a[i - 1]] = i

print((dp[N] - 1) % 1000000007)
