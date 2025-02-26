class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split()
        for i in range(len(strings)):
            strings[i] = strings[i][::-1]
        
        return ' '.join(strings)

        