class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        def distanceBetweenLetters(a, b):
            pos_a = ord(a.lower()) - ord('a')
            pos_b = ord(b.lower()) - ord('a')
            diff = pos_b - pos_a
            return diff if pos_b >= pos_a else (diff + 26)
        
        
        counter = defaultdict(lambda: 0)
        for i in range(len(s)):
            x = distanceBetweenLetters(s[i], t[i])

            if x == 0:
                continue
            og = x
            x += (counter[og] * 26)

            if x > k :
                return False
            
            counter[og] += 1
            # taken_i.add(x)
            
            
        return True