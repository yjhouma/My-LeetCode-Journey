class Solution:
    def check(self, nums: List[int]) -> bool:
        # is_rotated = True
        n = len(nums)
        idx_max = max(enumerate(nums), key=lambda x: x[1])[0]
        next_idx_max = (idx_max+1)%n
        counter = 0

        while nums[next_idx_max] == nums[idx_max] and counter < n:
            idx_max = next_idx_max
            next_idx_max  = (idx_max+1)%n
            counter += 1

        if counter == n:
            return True



        idx_start = (idx_max + 1) % n
        curr_num = nums[idx_start]

        while idx_start != idx_max:

            next_idx = (idx_start + 1)%n
            next_num = nums[next_idx]
            if curr_num > next_num:
                return False
            
            curr_num = next_num
            idx_start = next_idx
        
        return True