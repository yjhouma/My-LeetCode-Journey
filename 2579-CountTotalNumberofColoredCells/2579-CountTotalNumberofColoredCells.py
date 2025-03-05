class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 
        # 1 + 4, 
        # 1 + 4 + 8, 
        # 1 + 4 + 8 + 12 =25
        # 1 + 4 + 8 + 12 + 16 = 41

        '''
            n = 5
            nderet = 4
            Sn = n/2 * (an + un)
            un = 4*nderet
            an = 4
            Sn = nderet
        '''
        if n == 1:
            return 1
        
        n -= 1

        return 1 + ((n*(4+4*n))//2)    