class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_change = k
        idx = 0
        while idx < len(blocks) - k +1:
            c = Counter(blocks[idx:idx+k])

            min_change = min(min_change, c['W'])
            idx +=1
        
        return min_change