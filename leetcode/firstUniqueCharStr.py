# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in s:
#             if s.count(i) == 1:
#                 return s.index(i)

#         return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i

        return -1


sol = Solution()
print(sol.firstUniqChar("loveleetcode"))
