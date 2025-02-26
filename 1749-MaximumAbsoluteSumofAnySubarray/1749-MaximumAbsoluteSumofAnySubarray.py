class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min = curr_max = nums[0]
        res_max =  curr_max
        res_min = curr_min

        for i in range(1,len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            curr_min = min(curr_min + nums[i], nums[i])

            res_max = max(curr_max, res_max)
            res_min = min(curr_min, res_min)

        return max(abs(res_max),abs(res_min))