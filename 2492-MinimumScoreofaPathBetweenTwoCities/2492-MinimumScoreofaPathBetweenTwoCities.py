class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roots = list(range(n+1))

        
        def find_roots(node):
            if roots[node] == node:
                return node
            roots[node] = find_roots(roots[node])

            return roots[node]
        
        for u,v,w in roads:
            root1, root2 = find_roots(u), find_roots(v)

            if root1 == root2:
                continue
            roots[root2] = root1
        
        base = find_roots(1)
        min_w = inf
        for u,v,w in roads:
            root2 = find_roots(u)
            if base == root2:
                min_w = min(min_w,w)
        
        return min_w
