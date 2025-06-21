class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        
        n = len(nums)
        
        ans = [1] * n

        left = 1
        right = 1

        for i in range(n):
            ans[i] *= left
            left *= nums[i]
        for j in range(n - 1, -1 ,-1):
            ans[j] *= right
            right *= nums[j]
        return ans
