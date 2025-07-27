class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1 and k == 1:
            return [[1]]

        result = []

        def backtracking(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()

        backtracking(1, [])
        return result
