class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        repeated = None
        all_nums = set(range(1,1+n**2))
        appeared_num = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] in appeared_num:
                    repeated = grid[i][j]
                
                appeared_num.add(grid[i][j])
        
        return [repeated, (all_nums-appeared_num).pop()]
        