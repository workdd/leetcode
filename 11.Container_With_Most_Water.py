class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            l = height[left]
            r = height[right]

            h = min(l, r)
            ans = max(ans, h * (right - left))
            if l <= r:
                left += 1
            elif r < l:
                right -= 1

        return ans
