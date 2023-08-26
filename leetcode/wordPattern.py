class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dum = s.split(" ")
        dict = {}
        for i in range(len(pattern)):
            dict[pattern[i]] = dum[i]

        print(dict)


sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))
