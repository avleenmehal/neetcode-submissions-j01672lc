class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        sorted_edges = sorted([sorted(edge) for edge in edges])
        print(sorted_edges)
        for l,r in sorted_edges:
            adj[l].append(r)
            adj[r].append(l)
        

        visited = set()

        def dfs(node, par):
            print(visited)
            if node in visited:
                return False

            visited.add(node)
            print(node)
            for child in adj[node]:
                if child == par:
                    continue
                print("nodes", node, "child", child)

                if not dfs(child, node):
                    return False

            return True
        

        if dfs(0,-1) and len(visited) == n:
            return True
        return False