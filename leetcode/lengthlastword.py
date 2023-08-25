class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([x for x in s.split()][-1])


sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
