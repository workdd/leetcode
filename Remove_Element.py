class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer1 = 0
        pointer2 = len(nums)

        while pointer1 < pointer2:
            if nums[pointer1] == val:
                del nums[pointer1]
                pointer2-=1
            else:
                pointer1 +=1

    
