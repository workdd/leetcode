class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(nums) - 1

        set_dict = {}
        is_checked = False
        while pointer1 <= pointer2:
            for key, val in set_dict.items():
                if nums[pointer1] == key:
                    if val >= 2:
                        del nums[pointer1]
                        is_checked = True
                        pointer2 -=1
                        break

            if is_checked:
                is_checked = False
                continue
            else:
                if nums[pointer1] not in set_dict:
                    set_dict[nums[pointer1]] = 1
                else:
                    set_dict[nums[pointer1]] +=1
            pointer1+=1
