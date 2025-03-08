class MedianFinder:

    def __init__(self):
        self.nums = []
        self.median = None
        self.nums_length = 0
        

    def addNum(self, num: int) -> None:

        if self.nums_length == 0:
            self.nums.append(num)
            self.median = num
            self.nums_length += 1
            return
        
        self.nums.append(num)
        self.nums_length += 1

        
        

    def findMedian(self) -> float:
        self.nums = sorted(self.nums)
        if self.nums_length % 2 ==1:
            self.median = self.nums[self.nums_length//2]
        else:
            self.median = self.nums[self.nums_length//2] + self.nums[self.nums_length//2 - 1]
            self.median /= 2
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()