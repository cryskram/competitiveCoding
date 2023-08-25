class Solution:
    def fizzBuzz(self, n: int) -> list:
        dum = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                dum.append("FizzBuzz")
            else:
                if i % 3 == 0:
                    dum.append("Fizz")
                elif i % 5 == 0:
                    dum.append("Buzz")
                else:
                    dum.append(str(i))

        return dum


sol = Solution()
print(sol.fizzBuzz(15))
