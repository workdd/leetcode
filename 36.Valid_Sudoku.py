class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}

        boxes = {}
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]

                if num == ".":
                    continue

                if i not in rows:
                    rows[i] = {}
                if num in rows[i]:
                    return False
                rows[i][num] = True

                if j not in cols:
                    cols[j] = {}
                if num in cols[j]:
                    return False
                cols[j][num] = True

                box_index = (i // 3, j // 3)

                if box_index not in boxes:
                    boxes[box_index] = {}
                if num in boxes[box_index]:
                    return False
                boxes[box_index][num] = True

        return True
