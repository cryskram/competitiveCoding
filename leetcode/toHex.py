class Solution:
    def toHex(self, num: int) -> str:
        return str(hex(num))[2:]


sol = Solution()
print(sol.toHex(-1))
