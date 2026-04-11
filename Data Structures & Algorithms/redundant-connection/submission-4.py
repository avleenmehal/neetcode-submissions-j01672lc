class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]

        rank = [1] * (len(edges)+1)

        def find(src):
            p = par[src]
            while p != par[p]:
                par[p]=par[par[p]]
                p = par[p]
            return p

        def union(u,v):
            p1,p2 = find(u),find(v)
            if p1 == p2:
                return True
            
            if rank[p1]> rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return False


        for u,v in edges:
            if union(u,v):
                return [u,v]
        

        