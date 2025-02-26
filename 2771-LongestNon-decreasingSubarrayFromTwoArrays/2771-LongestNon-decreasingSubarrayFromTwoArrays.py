class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # If we take num1 how long is the length
        # If we take num2 how long is the length
        
        # ltn21 = ltn11 = ltn12 = ltn22 = 1
        route1= route2 = maxl = 1

        for i in range(1,len(nums1)):
            ltn21 = 1+route2 if nums2[i-1] <= nums1[i] else 1
            ltn11 = 1+route1 if nums1[i-1] <= nums1[i] else 1
            ltn22 = 1+route2 if nums2[i-1] <= nums2[i] else 1
            ltn12 = 1+route1 if nums1[i-1] <= nums2[i] else 1

            route1 = max(ltn21, ltn11)
            route2 = max(ltn22, ltn12)
            maxl = max(maxl, route1, route2)
        
        return maxl





        curr_length=1
        max_length=1
        prev_num = min(nums1[0], nums2[0])
        n = len(nums1)
        for i in range(1,n):
            if nums1[i] >= prev_num and nums2[i] >= prev_num:
                k = min(nums1[i], nums2[i])
            elif nums1[i] >= prev_num:
                k = nums1[i]
            elif nums2[i] >= prev_num:
                k = nums2[i]
            else:
                k = -1


            if k >= prev_num:
                curr_length += 1
                prev_num = k
                continue
            
            max_length = max(max_length, curr_length)
            prev_num = k
            curr_length = 1
        
        return max(max_length,curr_length)
        