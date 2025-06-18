class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lst = nums1[:m]
        lst2 = nums2[:n]
        nums1[:] = lst + lst2
        nums1.sort()
