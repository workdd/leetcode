class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        cnt = 0
        ans = 100001

        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            cnt += 1
            while current_sum >= target:
                ans = min(ans, cnt)
                current_sum -= nums[left]
                left += 1
                cnt -= 1

        if ans == 100001:
            ans = 0
        return ans
