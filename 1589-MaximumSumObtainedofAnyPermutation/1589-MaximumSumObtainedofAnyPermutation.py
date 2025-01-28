class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums = sorted(nums,reverse=True)
        n = len(nums)
        freq = [0]*(n+1)

        for r in requests:
            freq[r[0]] += 1
            freq[r[1]+1] -= 1
        
        # Sweeping
        for i in range(1,n+1):
            freq[i] += freq[i-1]
        
        sorted_freq = sorted(freq, reverse=True)
        ret = 0 
        
        for x,y in zip(sorted_freq,nums):
            ret += ((x*y) % (1_000_000_007))

        return ret % 1_000_000_007

        