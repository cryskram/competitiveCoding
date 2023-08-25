# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n % 2 != 0 and n != 1:
#             return False
#         else:
#             for i in range(n):
#                 if 2**i == n:
#                     return True
#                 else:
#                     continue

#         return False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1

        return count == 1


sol = Solution()
print(sol.isPowerOfTwo(1))
