class Solution:
     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build adjacency list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()   # recursion stack (cycle detection)
        visited = set()    # memoization (already safe)

        def dfs(crs):

            # cycle found
            if crs in visiting:
                return False

            # already checked → no need to recompute
            if crs in visited:
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)   # mark safe

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True