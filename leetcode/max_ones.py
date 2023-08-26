# not working


class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == 1:
                count += 1
                if nums[i + 1] == 1:
                    count += 1
            else:
                count = 0
                continue

        return count


sol = Solution()
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
