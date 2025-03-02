# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        l , r = 1, n

        midpoint = n//2
        while True:
            A = isBadVersion(midpoint-1)
            B = isBadVersion(midpoint)

            if  not A and B:
                return midpoint
            
            if B:
                r = midpoint -1
                midpoint = (l+r) // 2
            else:
                l = midpoint + 1
                midpoint = (l+r)//2



        # A = 1==1
        # print(not A)
        return 0