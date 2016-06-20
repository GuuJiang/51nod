import bisect

n = int(input())
s = [int(input()) for i in range(n)]

result = 1
dp = [10000000000] * n
dp[0] = s[0]
for i in s:
    if i > dp[result - 1]:
        dp[result] = i
        result += 1
    else:
        pos = bisect.bisect(dp, i)
        dp[pos] = i

print(result)
