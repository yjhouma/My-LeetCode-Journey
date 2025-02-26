import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nqueue = []
        for n in nums:
            heapq.heappush(nqueue, -1*n)

        score = 0
        for i in range(k):
            curr_score = heapq.heappop(nqueue)
            score += (-1*curr_score)
            heapq.heappush(nqueue, curr_score//3)
        
        return score

        