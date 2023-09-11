class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        dum = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    dum.append(i)

        elif len(nums2) > len(nums1):
            for i in nums1:
                if i in nums2:
                    dum.append(i)

        else:
            for i in nums1:
                if i in nums2:
                    dum.append(i)

        return dum


print(Solution().intersect([3, 1, 2], [1, 1]))
