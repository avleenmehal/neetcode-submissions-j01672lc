class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(u):
            p = par[u]
            while p!= par[p]:
                par[p] = par[par[p]]
                p=par[p]
            
            return p

        def union(n1,n2):
            u,v = find(n1), find(n2)
            if u==v:
                return False
            
            if rank[u] > rank[v]:
                rank[u]+=rank[v]
                par[v]=u
            else:
                rank[v]+=rank[u]
                par[u]=v
            
            return True

        res = n
        for n1,b2 in edges:
            if union(n1,b2):
                res -=1
        return res