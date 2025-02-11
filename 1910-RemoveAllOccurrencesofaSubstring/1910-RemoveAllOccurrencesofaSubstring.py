class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s.find(part) != -1:
            pos = s.find(part)
            end = pos + len(part)

            print(s[pos:end])
            # s[pos:end] = ''
            s = s[:pos] + s[end:]
            # print(s)

        return s
        