class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        sub_string = ""
        max_length = 0
        while start <= end and end < len(s):
            if s[end] not in sub_string:
                sub_string += s[end]
                end += 1
                max_length = max(max_length, len(sub_string))
            else:
                start += 1
                end = start
                sub_string = ""
        return max_length
