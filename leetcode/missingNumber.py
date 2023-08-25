# buggy


class Solution:
    def missingNumber(self, nums: list) -> int:
        n = len(nums)
        nums.sort()
        for i in range(nums[0], n):
            if i == nums[i]:
                print(i)
            else:
                print(i)


sol = Solution()
print(sol.missingNumber([0, 1]))
