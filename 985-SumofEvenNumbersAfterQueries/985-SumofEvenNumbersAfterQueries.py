class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_total = 0
        for n in nums:
            if n%2 == 0:
                sum_total += n
        ans = []
        for val, idx in queries:
            prev_val = nums[idx]
            new_val = prev_val + val
            if prev_val%2 == 0 and new_val%2 == 0:
                sum_total += val
            elif prev_val%2 == 0 and new_val%2 == 1:
                sum_total -= prev_val
            elif prev_val%2 == 1 and new_val%2 == 0:
                sum_total += new_val
            ans.append(sum_total)
            nums[idx] = new_val
        
        return ans