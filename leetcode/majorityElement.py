class Solution:
    def majorityElement(self, nums: list) -> int:
        for i in set(nums):
            if nums.count(i) > len(nums) / 2:
                return i

        return -1


sol = Solution()
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
