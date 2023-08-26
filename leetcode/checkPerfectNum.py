# works for small numbers


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        val = sum(i for i in range(1, num) if num % i == 0)

        return val == num


sol = Solution()
print(sol.checkPerfectNumber(28))
