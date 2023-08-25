class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        else:
            dum = ""
            num = x
            while num > 0:
                dig = num % 10
                dum += str(dig)
                num //= 10

            return True if dum == str(x) else False


sol = Solution()

print(sol.isPalindrome(0))
