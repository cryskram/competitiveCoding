class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = list(set(s))
        y = list(set(t))

        for i in x:
            if i not in y:
                return False

        return True


sol = Solution()
print(sol.isSubsequence("abc", "hbgdc"))
