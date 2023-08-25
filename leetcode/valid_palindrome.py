class Solution:
    def isPalindrome(self, s: str) -> bool:
        dum = ""
        for i in s.lower():
            if i.isalnum():
                dum += i
            else:
                continue

        return True if dum == dum[::-1] else False


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
