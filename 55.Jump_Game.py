class Solution:
    def canJump(self, nums: List[int]) -> bool:
        is_jumped = 0

        for idx,val in enumerate(nums):
            if idx > is_jumped:
                return False
            is_jumped = max(is_jumped, idx + val)

        if is_jumped >= len(nums) - 1:
            return True
        else:
            return False

        
