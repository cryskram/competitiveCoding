class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        pos = []
        sum = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                sum = nums[i] + nums[j]
                if sum == target and i != j:
                    pos.append(i)
                    pos.append(j)

        pos.pop()
        pos.pop()

        return pos


solution = Solution()

print(solution.twoSum([3, 2, 4], 6))
