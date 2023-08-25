class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == reversed(s) else False


sol = Solution()

print(sol.isPalindrome(121))
