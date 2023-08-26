class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        for i in nums:
            if i == val:
                nums.remove(i)

        return nums


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
