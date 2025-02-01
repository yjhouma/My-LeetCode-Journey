class Solution:
    def round_down_to_nearest_10(self,num, n):
        pw = 10**n
        return (num//pw) * pw
    
    def is_monotone_increasing(self,n):
        dgt = 0
        while n>1:
            curr_digit = n%10
            n = n//10
            prev_digit = n%10
            dgt += 1
            if prev_digit > curr_digit:
                return False
        
        return True

    def monotoneIncreasingDigits(self, n: int) -> int:

        pw = 1
        while not self.is_monotone_increasing(n):
            n = self.round_down_to_nearest_10(n, pw) - 1
            pw += 1

        
        return n

        
