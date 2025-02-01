class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Mark each node island
        n = len(grid)
        land_mark = [[0 for _ in range(n)] for _ in range(n)]
        visited = set()
        land_size = defaultdict(lambda: 0)
        
        shore = set()

        def update_land_mark(i,j,land_idx):
            q = deque()
            q.append((i,j))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            size = 0
            while q:
                r,c = q.pop()
                if (r,c) in visited:
                    continue
                land_mark[r][c] = land_idx
                size += 1
                visited.add((r,c))

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<n and 0<=nc<n:
                        if grid[nr][nc] == 1:
                            q.append((nr,nc))
                        else:
                            shore.add((nr,nc))
            return size
        
        land_idx = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # Update the land_mark
                    size = update_land_mark(i,j,land_idx)
                    land_size[land_idx] = size
                    land_idx += 1
    
            
        largest_island = 0
        if land_idx == 1:
            return 1
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i,j in shore:
            if grid[i][j] == 0:
                connected_island = []
                curr_size = 1
                for di, dj in directions:
                    ni = i +di
                    nj = j +dj
                    if 0<=ni<n and 0<=nj<n and land_mark[ni][nj]>0 and land_mark[ni][nj] not in connected_island:
                        curr_size += land_size[land_mark[ni][nj]]
                        connected_island.append(land_mark[ni][nj])
                largest_island = max(largest_island, curr_size)

        
        return largest_island if largest_island > 0 else n*n
