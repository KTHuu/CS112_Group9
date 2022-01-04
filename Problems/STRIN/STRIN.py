n = int(input())

MOD = int(1e9 + 7)

dp = [[0, 0, 0] for i in range(100001)]

dp[1][0] = dp[1][1] = dp[1][2] = 1

for len in range(2, n + 1):
    for last in range(3):
        dp[len][last] = dp[len-1][0] + dp[len-1][1] + dp[len-1][2]
        if last == 1:
            dp[len][last] = dp[len][last] - dp[len-1][1]
        dp[len][last] = dp[len][last] % MOD

res = dp[n][0] + dp[n][1] + dp[n][2]
res = res % MOD
print(res)
