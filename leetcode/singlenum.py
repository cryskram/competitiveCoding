class Solution:
    def singleNumber(self, nums: list) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i


sol = Solution()
print(sol.singleNumber([4, 1, 2, 1, 2]))
