class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = " ".join(s)

        s = s.split(" ")[::-1]

        s = " ".join(s)
        return s
