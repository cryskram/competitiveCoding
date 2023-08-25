class Solution:
    def thirdMax(self, nums: list) -> int:
        s = list(set(nums))
        s.sort()
        if len(s) == 2:
            return s[-1]
        elif len(s) == 3 or len(s) == 1:
            return s[0]
        else:
            return s[-3]


sol = Solution()
print(sol.thirdMax([1, 1, 1]))
