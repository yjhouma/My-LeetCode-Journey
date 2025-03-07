class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left ==1: left+=1
        prime = [True for i in range(right+1)]
        p = 2
        while (p*p <= right):
            if prime[p]:
                for i in range(p*p, right+1, p):
                    prime[i] =False 
            p += 1
        prime[0]=False
        prime[1]=False
        best_pair = [-1,-1]
        min_dist = None


        # print(prime[1])
        # print(prime[11])
        l, r = left, left+1
        
        while l <= right and r <= right:
            if prime[l] and prime[r]:
                curr_dist = r - l
                if min_dist is None or min_dist > curr_dist:
                    min_dist = curr_dist
                    best_pair = [l, r]
                
                l, r = r, r+1
            elif prime[l]:
                r +=1
            else:
                l += 1
                r = l+1
        
        return best_pair
