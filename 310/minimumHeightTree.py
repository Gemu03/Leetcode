from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:  return [0]
        g=[set() for _ in range(n)]
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        leaves=[i for i in range(n) if len(g[i])==1]
        while n>2:
            n-=len(leaves)
            new_leaves=[]
            for leaf in leaves:
                neighbor=g[leaf].pop()
                g[neighbor].remove(leaf)
                if len(g[neighbor])==1:new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


s = Solution()
print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) # [1]
print(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) # [3,4]
print(s.findMinHeightTrees(1, [])) # [0]