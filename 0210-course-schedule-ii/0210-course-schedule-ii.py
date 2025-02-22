class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        al = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            al[i].append(j)

        visit, path = set(), set()
        output = []

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)

            for n in al[crs]:
                if not dfs(n): return False
            
            visit.add(crs)
            output.append(crs)
            path.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i) and i not in visit:
                return []
        
        return output
        
        