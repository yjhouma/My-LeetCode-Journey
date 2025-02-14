class ProductOfNumbers:

    def __init__(self):
        self.mem = [1]
        self.num_in_mem = 1
        self.zero_exist_in = None


    def add(self, num: int) -> None:  
        if num == 0:
            num_add = 1
            self.zero_exist_in = self.num_in_mem
        else:
            num_add = self.mem[-1]*num
    
        self.mem.append(num_add)
        self.num_in_mem += 1
        

    def getProduct(self, k: int) -> int:
        r = self.num_in_mem-1
        l = max(0,self.num_in_mem-k-1)
        if self.zero_exist_in is not None and l < self.zero_exist_in <=r:
            return 0
        return self.mem[r] // self.mem[l]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)