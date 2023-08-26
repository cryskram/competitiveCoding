class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x, y = list(s), list(t)
        x.sort()

        # length of y is always greater than x
        x.append(" ")
        y.sort()

        for i in range(len((y))):
            if x[i] != y[i]:
                return y[i]


sol = Solution()
print(sol.findTheDifference("", "y"))
