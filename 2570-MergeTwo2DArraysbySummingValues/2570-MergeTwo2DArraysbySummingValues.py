class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        idx_nums1 = idx_nums2 = 0
        n = len(nums1)
        m = len(nums2)
        ret = []
        while idx_nums1 < n or idx_nums2 < m:
            if idx_nums2 >= m:
                ret.append(nums1[idx_nums1])
                idx_nums1 += 1
            elif idx_nums1 >= n:
                ret.append(nums2[idx_nums2])
                idx_nums2 += 1
            elif nums1[idx_nums1][0] < nums2[idx_nums2][0]:
                ret.append(nums1[idx_nums1])
                idx_nums1 += 1
            elif nums2[idx_nums2][0] < nums1[idx_nums1][0]:
                ret.append(nums2[idx_nums2])
                idx_nums2 += 1
            else:
                n1 = nums1[idx_nums1]
                n2 = nums2[idx_nums2]
                ret.append([n1[0], n1[1] +n2[1]])
                idx_nums2 += 1
                idx_nums1 += 1
        return ret

        