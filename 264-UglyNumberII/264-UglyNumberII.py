import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Use heap because we want to add it one by one from the smallest value
        pq = [1]
        primes = [2,3,5]
        curr_n = 0
        already_out = set()
        already_out.add(1)
        while curr_n < n:
            curr_num = heapq.heappop(pq)
            for p in primes:
                next_num = curr_num * p
                if next_num not in already_out:
                    heapq.heappush(pq, next_num)
                    already_out.add(next_num)
            
            curr_n += 1
        
        return curr_num
        
        