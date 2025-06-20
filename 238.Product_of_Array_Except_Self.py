class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []

        init_num = 1
        for idx, num in enumerate(nums):
            for i in range(len(nums)):
                if idx != i:
                    init_num *= nums[i]
            lst.append(init_num)
            init_num = 1
        return lst
