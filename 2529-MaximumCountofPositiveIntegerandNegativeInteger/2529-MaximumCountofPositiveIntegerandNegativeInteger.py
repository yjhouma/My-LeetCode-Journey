class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Use binary Search to find the first negative number.
        negative_exist = nums[0] < 0
        positive_exist = nums[-1] > 0

        n = len(nums)
        if nums[0]> 0 or nums[-1] <0:
            return n
        
        neg = -1
        pos = n+1
        # If negative exist find the last negative number using binary search
        if negative_exist:
            l = 0
            r = n-1
            while l <= r:
                mid_point = (l+r)//2
                if nums[mid_point] < 0 and nums[mid_point+1] >= 0:
                    neg = mid_point
                    break
                
                if nums[mid_point] < 0:
                    l = mid_point + 1
                else:
                    r = mid_point - 1
            
        if positive_exist:
            l = 0 if neg is None else neg+1
            r = n-1

            while l <= r:
                mid_point = (l+r)//2
                if nums[mid_point] > 0 and nums[mid_point-1] <= 0:
                    pos = mid_point
                    break
                
                if nums[mid_point] > 0:
                    r = mid_point - 1
                else:
                    l = mid_point + 1
        



        return max(neg+1, n-pos)
