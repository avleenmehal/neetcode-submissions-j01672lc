class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        visiting = set()
        visited = set()
        order = []

        def dfs(crs):
            if crs in visiting:
                return False

            if preMap[crs] == []:
                if crs not in visited:
                    order.append(crs)
                visited.add(crs)
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            if crs not in visited:
                    order.append(crs)
            visiting.remove(crs)
            visited.add(crs)
            preMap[crs]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return order
        