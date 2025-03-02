class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n ==2:
            return 2
    
        ways_to_climb = [1,2]
        for i in range(2,n):
            ways = ways_to_climb[i-1] + ways_to_climb[i-2]
            ways_to_climb.append(ways)
        
        return ways