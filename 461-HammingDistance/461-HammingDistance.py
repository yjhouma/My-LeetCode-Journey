class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        new_num = x^y
        return bin(x^y).count('1')
        