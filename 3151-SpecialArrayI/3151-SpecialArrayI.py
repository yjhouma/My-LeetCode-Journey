class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_parity = nums[0] % 2

        for i in range(1, len(nums)):
            curr_parity = nums[i] % 2
            if prev_parity == curr_parity:
                return False
            prev_parity = curr_parity
        
        return True
        
