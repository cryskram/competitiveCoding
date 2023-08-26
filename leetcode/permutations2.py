from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list) -> list[list]:
        d = list(set(permutations(nums, len(nums))))
        return d


print(Solution().permuteUnique([1, 2, 3]))
