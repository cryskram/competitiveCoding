class Solution:
    def moveZeroes(self, nums: list) -> None:
        iLen = len(nums)
        try:
            for i in range(len(nums)):
                nums.pop(nums.index(0))
        except ValueError:
            pass

        for i in range(iLen - len(nums)):
            nums.append(0)

        print(nums)


sol = Solution()
print(sol.moveZeros([0, 1, 0, 3, 12]))
