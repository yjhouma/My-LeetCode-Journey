class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # i < j so the maximum pair is only on the left
        spots = len(values)
        score_dp = [0] * spots
        # score_dp[-1] = values[-1]
        score_dp[-2] = values[-1]-1
        max_score = 0
        for i in range(spots-2,-1,-1):
            score_dp[i] = max(values[i+1]-1, score_dp[i+1]-1)
            curr_score = values[i] + score_dp[i]
            max_score = curr_score if max_score < curr_score else max_score
        print(score_dp)
        return max_score


        