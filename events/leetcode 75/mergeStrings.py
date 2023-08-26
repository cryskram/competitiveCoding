class Solution:
    def mergeAlternately(Self, word1: str, word2: str) -> str:
        dum = ""
        try:
            for i in range(len(word1) + len(word2)):
                dum += word1[i] + word2[i]
        except IndexError:
            pass

        return dum


sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))
