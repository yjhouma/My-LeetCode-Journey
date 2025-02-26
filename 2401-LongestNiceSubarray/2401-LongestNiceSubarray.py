class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # (num1 OR num2) AND num3
        curr_or = nums[0]
        first_idx = 0
        max_substring = 1
        curr_substring = 1
        for i in range(1,len(nums)):
            if curr_or & nums[i] == 0:
                curr_substring += 1
                curr_or = curr_or ^ nums[i]
            else:
        
                max_substring = max(max_substring, curr_substring)
                while (curr_or & nums[i] != 0):
                    curr_or = curr_or ^ nums[first_idx]
                    curr_substring -= 1
                    
                    first_idx += 1
            
                curr_or = curr_or ^ nums[i]
                curr_substring += 1

                
                # curr_substring = 1
                # curr_or = n
        
        return max(max_substring,curr_substring)




        