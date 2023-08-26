# not working


class Solution:
    def maxArea(sed, height: list) -> int:
        if len(set(height)) == 1:
            return height[0]
        else:
            d = list(set(height))
            d.sort()
            return height[height.index(d[-2])] * len(
                range(height.index(d[-1]), height.index(height[-1]))
            )


print(Solution().maxArea([4, 3, 2, 1, 4]))
