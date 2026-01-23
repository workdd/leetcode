class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        visited = [-1] * numCourses

        def dfs(node):
            if visited[node] == 0:
                return False
            if visited[node] == 1:
                return True

            visited[node] = 0

            for n in graph[node]:
                if not dfs(n):
                    return False

            visited[node] = 1
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
