class Solution:
    def reverseString(self, s: list) -> None:
        d = list(s)
        d.reverse()
        return d


sol = Solution()
print(sol.reverseString(["h", "e", "l", "l", "o"]))
