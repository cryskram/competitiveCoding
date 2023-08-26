from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list]:
        d = list(combinations(range(1, n + 1), k))
        return d


print(Solution().combine(4, 2))
