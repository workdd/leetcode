class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(nums) - 1
        
        set_list = []
        is_checked = False
        while pointer1 <= pointer2:
            for ele in set_list:
                if nums[pointer1] == ele:
                    is_checked = True
                    break
            
            if is_checked:
                del nums[pointer1]
                pointer2 -=1
                is_checked = False
            else:
                set_list.append(nums[pointer1])
                pointer1 +=1
                

            
