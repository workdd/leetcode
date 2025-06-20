class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        current_distance = 0
        cnt = 0
        num_jump = 0
        
        for idx in range(0, len(nums) - 1):
            num_jump = max(num_jump, idx + nums[idx])

            if idx == current_distance:
                cnt+=1
                current_distance = num_jump
        return cnt
        
            
