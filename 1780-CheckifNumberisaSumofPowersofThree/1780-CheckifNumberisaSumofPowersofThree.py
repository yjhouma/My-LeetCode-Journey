class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        can_substract = True
        while n > 0:
            if n%3 == 0:
                n //= 3
                can_substract = True
            elif can_substract:
                n -= 1
                can_substract = False
            else:
                return False
        
        return True

        