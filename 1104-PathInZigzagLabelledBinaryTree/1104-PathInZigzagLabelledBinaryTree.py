import math
class Solution:
    def find_number(self, pos,level):
        if level % 2 ==0:
            return pos + (2**(level)) - 1
        else:
            return (2**(level+1) - 1) - pos + 1

    def pathInZigZagTree(self, label: int) -> List[int]:
        

        ret = [label]
        level = math.floor(math.log2(label))
        if level % 2 == 0:
            pos = label - (2**(level)) + 1
        else:
            pos = (2**(level+1) - 1) - label + 1
        # parent_pos = (pos+1)//2
        # level -= 1



        while level > 0:
            level -= 1
            pos = (pos+1)//2
            # print(pos, level)
            ret.append(self.find_number(pos,level))
            





        return ret[::-1]

        