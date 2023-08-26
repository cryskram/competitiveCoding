class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        if x < 0:
            if int("-" + s[::-1]) not in range(-(2**31), 2**31):
                return 0
            else:
                return int("-" + s[::-1])
        elif x > 0:
            if int(s[::-1]) not in range(-(2**31), 2**31):
                return 0
            else:
                return int(s[::-1])
        elif s[-1] == 0:
            return int(s[::-1])
        else:
            return x


sol = Solution()
print(sol.reverse(-123))
