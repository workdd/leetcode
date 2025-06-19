class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            last_element = nums[-1]
            del nums[-1]
            nums.reverse()
            nums.append(last_element)
            nums.reverse()

            k-=1
