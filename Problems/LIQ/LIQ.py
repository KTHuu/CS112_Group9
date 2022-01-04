n = int(input())

a = [int(i) for i in input().strip().split()]

dp = [0] * 1003
res = 0

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if (a[j] < a[i]):
            dp[i] = max(dp[i], dp[j] + 1)
    res = max(res, dp[i])

print(res)
