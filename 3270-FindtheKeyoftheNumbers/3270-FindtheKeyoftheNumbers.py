class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num = 0
        mult = 1
        for _ in range(4):
            temp_num = min((num1%10), (num2%10), (num3%10))
            temp_num *= mult
            num += temp_num
            mult *= 10

            num1 //=10
            num2 //=10
            num3 //=10
        
        return num

        