class Solution:
    def removeDuplicates(self, nums: list) -> int:
        return len(sorted(set(nums))[:])


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
