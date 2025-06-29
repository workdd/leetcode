class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums.sort()
        left = 0
        right = 1
        minus = 0
        while right < len(nums):
            if nums[right - 1] == nums[right] - 1:
                right += 1
                longest = max(longest, right - left - minus)
            elif nums[right - 1] == nums[right]:
                right += 1
                minus += 1
            else:
                left = right
                right += 1
                minus = 0

        if longest == 0 and len(nums) >= 1:
            return 1
        return longest
