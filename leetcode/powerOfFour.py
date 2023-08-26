class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(20):
            if 4**i == n:
                return True

        return False


sol = Solution()
print(sol.isPowerOfFour(1))
