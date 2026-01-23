class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        answer = []
        is_target = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid - 1
                is_target = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if is_target != -1:
            answer.append(is_target)
            is_target = -1

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid + 1
                is_target = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if is_target != -1:
            answer.append(is_target)
            is_target = False
        if not answer:
            return [-1, -1]
        return answer
