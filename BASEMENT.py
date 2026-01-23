# 이진탐색
def binary_search(nums, target):
    left, right = 0, len(nums - 1)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# dfs 그리드
def dfs(grid, r, c):
    rows, cols = len(grid), len(grid[0])

    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] == 0:
        return

    grid[r][c] = 0

    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)


# bfs 최단거리
from collections import deque


def bfs(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c, 0)])  # (r, c, distance)
    visited = set()
    visited.add((start_r, start_c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))


# dp 기본
def dp(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 투포인터
def two_pointer(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []  # 못찾은 경우


# 투포인터 중복 제거 예제
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# 슬라이딩 윈도우
def sliding_window(s):
    left = 0
    seen = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


# 그래프 (인접 리스트)
def build_graph(n, edges):
    graph = [[] for _ in range(n)]

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph


def dfs_graph(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited)


# 스택
def valid_parentheses(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# 힙(우선순위 큐)
import heapq


def kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heap.heappop(heap)
    return heap[0]
