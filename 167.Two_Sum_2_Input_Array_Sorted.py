class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1

        while pointer1 < pointer2:
            current_sum = numbers[pointer1] + numbers[pointer2]
            if current_sum == target:
                return [pointer1 + 1, pointer2 + 1]
            elif current_sum > target:
                pointer2 -= 1
            else:
                pointer1 += 1
