# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find peak
        n = mountainArr.length()
        # cahche = {}
        r_bound = n-1
        l_bound = 0
        print(r_bound)

        mid_point = r_bound//2
        mid = mountainArr.get(mid_point)
        r = mountainArr.get(mid_point+1)
        l = mountainArr.get(mid_point-1)
        # cache[mid_point] =  mid
        print(l,mid,r)
        # cache[mid_point+1] = r
        # cache[mid_point]
        naik = (l<mid) and (mid<r)
        turun = (l>mid) and (mid>r)
        # print ()
        while naik or turun:
            if (l < mid) and (mid < r):
                # peak ada di kanan
                nmid = (mid_point + r_bound)//2
                if (mid_point + r_bound) %2 ==1:
                    nmid+=1
                l_bound = mid_point
                mid_point = nmid
            else:
                nmid = (mid_point + l_bound)//2
                if (mid_point + l_bound) %2 ==1:
                    nmid+=1
                r_bound = mid_point
                mid_point = nmid

            mid = mountainArr.get(mid_point)
            r = mountainArr.get(mid_point+1)
            l = mountainArr.get(mid_point-1)
            naik = (l<mid) and (mid<r)
            turun = (l>mid) and (mid>r)
        
        # return mid_point
        peak = mid_point
        # Find Left
        l = 0
        r = peak
        
        while l <= r:
            sol = (l+r)//2
            solval = mountainArr.get(sol)
            if solval < target:
                l = sol+1
            elif solval > target:
                r = sol-1
            else:
                return sol

        print('Cari di Kanan')
        # # Find Right
        l = peak
        r = n-1
        
        while l <= r:
            sol = (l+r)//2
            solval = mountainArr.get(sol)
            if solval > target:
                l = sol+1
            elif solval < target:
                r = sol-1
            else:
                return sol

        
        return -1


        
        