class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l<=r:
            midpoint = (l+r)//2
            if nums[midpoint] <  nums[midpoint-1]:
                return nums[midpoint]
            
            if nums[midpoint] > nums[r]:
                l = midpoint+1
            elif nums[midpoint] < nums[l]:
                # On lef
                r = midpoint-1
            elif nums[midpoint] > nums[l]:
                r = midpoint-1
        
        
            
            # return midpoint
        return -1

