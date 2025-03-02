class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # If only one row we can take the maximum value
        # DP SCORE[ROW][COL] + SCORE[ROW-1][COLS] - (COL-COLS)
        r = len(points)
        c = len(points[0])
        score_dp = [[0]* c for _ in range(r)]
        # Initiate Score First Row
        for i in range(c):
            score_dp[0][i] = points[0][i]

        # Update Score DP With max score to that cell
        for i in range(1,r):
            left = [0]*c
            left[0] = score_dp[i-1][0]
            right = [0]*c
            right[-1] = score_dp[i-1][-1]

            # print(left)
            for j in range(1,c):
                left[j] = max(score_dp[i-1][j], left[j-1]-1)
            
            for j in range(c-2,-1,-1):
                right[j] = max(score_dp[i-1][j], right[j+1]-1)
        
            for j in range(c):
                score_dp[i][j] = points[i][j] + max(left[j], right[j])


        print(score_dp)
        return max(score_dp[-1])