class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


sol = Solution()
print(sol.reverseWords("The sky is blue"))
