class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if graph[crs] == []:
                return True
            
            visitSet.add(crs)

            for a in graph[crs]:
                if not dfs(a):
                    return False
            visitSet.remove(crs)
            graph[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
    
        return True