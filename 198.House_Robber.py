class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-float("inf")] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[len(nums) - 1]
