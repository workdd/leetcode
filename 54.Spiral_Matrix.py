class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d_idx = 0
        row = len(matrix)
        col = len(matrix[0])
        length = len(matrix) * len(matrix[0])

        cycle = 0

        current_idx = [0, 0]
        while len(ans) < length:
            ans.append(matrix[current_idx[0]][current_idx[1]])
            if row > 1 and col > 1:
                if current_idx[1] == col - 1 - cycle and current_idx[0] != row - 1 - cycle:
                    d_idx = 1
                elif current_idx[0] == row - 1 - cycle and current_idx[1] == col - 1 - cycle:
                    d_idx = 2

                elif current_idx[0] == row - 1 - cycle and current_idx[1] == 0 + cycle:
                    d_idx = 3

                elif current_idx[0] == 1 + cycle and current_idx[1] == 0 + cycle:
                    d_idx = 0
                    if len(ans) >= length:
                        break
                    for j in range(row):
                        matrix[j] = matrix[j][1 : col - 1]
                    matrix = matrix[1 : row - 1]
                    row = len(matrix)
                    col = len(matrix[0])
                    current_idx[0], current_idx[1] = 0, -1
            if row > 1 and col == 1 and current_idx[1] != -1:
                d_idx = 1
            current_idx[0] += direction[d_idx][0]
            current_idx[1] += direction[d_idx][1]
        return ans
