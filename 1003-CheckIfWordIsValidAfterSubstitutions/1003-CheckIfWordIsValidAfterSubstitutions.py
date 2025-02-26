class Solution:
    def isValid(self, s: str) -> bool:
        
        while s != '':
            idx = s.find('abc')
            if idx == -1:
                return False
            s = s[:idx] + s[idx+3:]

        return True
        