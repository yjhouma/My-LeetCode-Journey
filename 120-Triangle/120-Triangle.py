class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for r in triangle:
            tmp = []
            for _ in r:
                tmp.append(0)
            dp.append(tmp)
        
        dp[0][0] = triangle[0][0]

        for r in range(1, len(triangle)):
            dp[r][0] = triangle[r][0] + dp[r-1][0]
            dp[r][-1] = triangle[r][-1] + dp[r-1][-1]
            for c in range(1,r):
                dp[r][c] = triangle[r][c] + min(dp[r-1][c], dp[r-1][c-1])
            
        # print(dp)
        return min(dp[-1])

        