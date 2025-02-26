class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        loi = []
        curr_length = 0
        prev_c = None
        start_index = 0
        end_index = 0
        for c in s:
            if prev_c is None:
                curr_length += 1
                prev_c = c
            elif c == prev_c:
                # print(c)
                curr_length += 1
                end_index += 1
                # print(curr_length)
            else:
                
                if curr_length >= 3:
                    # print(prev_c, curr_length)
                    # print(start_index, end_index)
                    loi.append([start_index, end_index])
                # print(c)
                curr_length = 1
                prev_c = c
                end_index += 1
                start_index = end_index
            
        if curr_length >= 3:
            # print(prev_c, curr_length)
            # print(start_index, end_index)
            loi.append([start_index, end_index])

        return loi