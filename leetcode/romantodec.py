class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0
        for i in s:
            if dict[i] > dict(s.index(i) + 1):
                print(True)
            else:
                print(False)


sol = Solution()

print(sol.romanToInt("MCMXCIV"))
