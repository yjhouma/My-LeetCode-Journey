class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_x = max_y = -1
        min_x = min_y = 51

        for t in towers:
            min_x = t[0] if t[0] < min_x else min_x
            max_x = t[0] if t[0] > max_x else max_x
            min_y = t[1] if t[1] < min_y else min_y
            max_y = t[1] if t[1] > max_y else max_y

        # print(max_x, min_x)
        # print(max_y, min_y)
        def distance(coor1, coor2):
            return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)**0.5
        
        def signal_strength(tower, coor, radius):
            d = distance((tower[0], tower[1]), coor)
            return int(tower[2]/(1+d)) if d <= radius else 0
        

        max_q = 0
        coor_max = [0,0]
        for x, y in itertools.product(range(min_x,max_x+1),range(min_y,max_y+1)):
            curr_q = 0
            for t in towers:
                curr_q += signal_strength(t, (x,y), radius)
            
            if curr_q > max_q:
                max_q = curr_q
                coor_max = [x, y]



        return coor_max
        

        
