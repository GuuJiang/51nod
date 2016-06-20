M, N = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]
dp = [[[0] * (M + 1) for i in range(M + 1)] for j in range(M + N)]
dp[1][1][1] = A[0][0]
for step in range(1, M + N):
    for x1 in range(max(step - N + 1, 1), min(step + 1, M + 1)):
        for x2 in range(max(step - N + 1, 1), min(step + 1, M + 1)):
            # print("dp[%d][%d][%d]=" % (step, x1, x2), end='')
            m = max(dp[step - 1][x1][x2], dp[step - 1][x1 - 1][x2],
                    dp[step - 1][x1][x2 - 1], dp[step - 1][x1 - 1][x2 - 1])
            if x1 == x2:
                dp[step][x1][x2] = m + A[step - x1][x1 - 1]
            else:
                dp[step][x1][x2] = m + A[step - x1][x1 - 1] + A[step - x2][x2 - 1]
            # print(dp[step][x1][x2])

print(dp[-1][-1][-1])
