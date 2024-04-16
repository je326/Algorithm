import sys
input = sys.stdin.readline

str1 = " " + input().strip()
str2 = " " + input().strip()
str3 = " " + input().strip()

len1, len2, len3 = len(str1), len(str2), len(str3)

dp = [[[0] * len3 for _ in range(len2)] for _ in range(len1)]
backTrack = [[[False] * len3 for _ in range(len2)] for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        for k in range(1, len3):
            if str1[i] == str2[j] == str3[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                backTrack[i][j][k] = True
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len1-1][len2-1][len3-1])