class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = m - i
        for j in range(n+1):
            dp[m][j] = n - j
        for i in range(m - 1,-1,-1):
            for j in range(n - 1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i + 1][j + 1],dp[i+1][j],dp[i][j+1])+1
        return dp[0][0]