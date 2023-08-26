# working but not the solution


class Solution:
    def findRelativeRanks(self, score: list) -> list:
        dum = []
        dict = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }
        score.sort(reverse=True)
        for i in range(1, len(score) + 1):
            if i in dict.keys():
                dum.append(dict[i])
            else:
                dum.append(str(i))

        return dum


sol = Solution()
print(sol.findRelativeRanks([5, 4, 3, 2, 1]))
