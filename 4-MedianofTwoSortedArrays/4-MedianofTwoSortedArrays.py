class Solution:



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length_total = len(nums1) + len(nums2)
        m = len(nums1)
        n = len(nums2)

        # if n == 0:
        #     return 


        idx = 0
        mid_point = length_total//2

        curr_num = None
        prev_num = None
        i1,i2 = 0,0
        while idx <= mid_point:
            prev_num = curr_num
            if i1 >= m:
                curr_num = nums2[i2]
                i2 += 1

            elif i2 >= n:
                curr_num = nums1[i1]
                i1 += 1

            elif nums1[i1] < nums2[i2]:
                curr_num = nums1[i1]
                i1 += 1
            else:
                curr_num = nums2[i2]
                i2 += 1
            
            idx += 1
        
        if length_total % 2 == 1:
            return curr_num/1.0
        else:
            return (curr_num + prev_num)/2.0
                

        
