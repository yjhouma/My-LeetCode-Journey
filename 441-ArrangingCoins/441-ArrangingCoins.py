class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Un/2 * (1 + Un) <= n
        # 2n = Un(1+Un)
        # Un + Un^2 = 2n
        # Un^2 + Un - 2n <= 0
        # B^2 - 4ac  = 1 - 4(1)(-2n) = 1+8n 
        # Un = (-1 + SQRT(1+ 8n))/2
        return floor((-1 + (1 + 8*n)**0.5)/2)
