class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        rt = num**0.5
        return int(rt) ** 2 == num


sol = Solution()
print(sol.isPerfectSq(16))
