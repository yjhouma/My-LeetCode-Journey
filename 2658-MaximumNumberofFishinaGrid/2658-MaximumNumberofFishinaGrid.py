class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Chekc up down left right
        num_fish = 0

        m = len(grid)
        n = len(grid[0])
        
        visited = []

        for i in range(m):
            for j in range(n):
                stack = []
                if (i,j) in visited:
                    continue
                
                visited.append((i,j))

                if grid[i][j] == 0:
                    continue

                
                # Check up
                stack.append((i,j))
                curr_fish = grid[i][j]
                while stack:
                    i0, j0 = stack.pop()
                    directions = [(1,0), (-1,0), (0,1), (0,-1)]
                    for d in directions:
                        ni, nj = i0+d[0], j0+d[1]
                        if 0 <=ni<m and 0<=nj<n and (ni,nj) not in visited and grid[ni][nj] > 0:
                            stack.append((ni,nj))
                            visited.append((ni,nj))
                            curr_fish += grid[ni][nj]
                
                num_fish = max(num_fish, curr_fish)
        
        return num_fish
