class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        num = points[0][1]
        cnt = 1
        for idx, point in enumerate(points, 1):
            if num >= point[0]:
                continue
            cnt += 1
            num = point[1]

        return cnt
