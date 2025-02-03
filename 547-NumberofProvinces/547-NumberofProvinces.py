class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Find Union to The rescue!!!!
        n = len(isConnected)
        roots = list(range(n))

        def find_root(node):
            if roots[node] == node:
                return node
            roots[node] = find_root(roots[node])
            return roots[node]
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    root1, root2 = find_root(i), find_root(j)
                    roots[root2] = root1
        

        province = set()
        for i in range(n):
            root_now = find_root(i)
            province.add(root_now)
        return len(province)