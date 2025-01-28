class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = [i[0] for i in sorted(enumerate(nums), key= lambda x: x[1])]
        l = 0
        r = len(n)-1

        while l<r:
            two_sum = nums[n[l]] + nums[n[r]]
            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            else:
                return [n[l],n[r]]

        return [] 