# partially works


class Solution:
    def findErrorNums(self, nums: list) -> list:
        d = 0
        for i in set(nums):
            if nums.count(i) > 1:
                d = i

        return [d, d + 1]
