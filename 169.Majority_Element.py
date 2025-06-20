class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt_dict = {}
        max_num =0 

        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 1
            else:
                cnt_dict[num] += 1

        max_cnt = 0
        for key, val in cnt_dict.items():
            if val > max_cnt:
                max_cnt = val
                max_num = key
        return max_num
