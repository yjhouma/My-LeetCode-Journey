class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)

        curr_target = ord('a')
        print(chr(curr_target))

        curr_length = longest = 0

        idx = 0
        while idx < n:
            curr_chr = ord(s[idx])
            if curr_chr == curr_target:
                curr_length += 1
                curr_target += 1
            else:
                longest = max(longest, curr_length)
                curr_length = 1
                curr_target = curr_chr + 1
        

            idx += 1




        return max(longest,curr_length)
            

        