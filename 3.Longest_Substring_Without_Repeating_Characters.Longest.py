class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        ans = 0
        for right, text in enumerate(s):
            if text not in lst:
                lst.append(text)
                ans = max(ans, len(lst))
            else:
                while text in lst:
                    lst = lst[1:]
                    ans = max(ans, len(lst))
                lst.append(text)
        return ans
