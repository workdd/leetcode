from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        adjacent = deque([])
        is_fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    adjacent.append([r, c])
                elif grid[r][c] == 1:
                    is_fresh += 1

        if is_fresh == 0:
            return 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        adjacent_cnt = -1
        temp_lst = []
        while temp_lst or adjacent and is_fresh:
            q = adjacent.popleft()
            r, c = q[0], q[1]

            for d in directions:
                dr = r + d[0]
                dc = c + d[1]
                if dr < 0 or dc < 0 or dr > rows - 1 or dc > cols - 1:
                    continue

                elif grid[dr][dc] == 1:
                    grid[dr][dc] = 2
                    temp_lst.append([dr, dc])
            if not adjacent:
                adjacent = deque(temp_lst)
                temp_lst = []
                adjacent_cnt += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return adjacent_cnt
