from itertools import permutations


class Solution:
    def permute(self, nums: list) -> list[list]:
        d = list(permutations(nums, len(nums)))
        return d


print(Solution().permute([1, 1, 2]))
