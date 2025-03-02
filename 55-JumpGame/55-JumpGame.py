class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = None
        target = len(nums)-1
        for i,n in enumerate(nums):
            if furthest is None:
                furthest = i + n

            if i > furthest and furthest != target:
                return False
            
            if furthest >= target:
                return True
                
            furthest = max(furthest, i+n)

            

    
        return furthest >= target
