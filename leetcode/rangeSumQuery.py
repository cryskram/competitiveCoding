class NumArray:
    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, left: int, right: int):
        count = 0
        for i in range(left, right + 1):
            count += self.nums[i]

        return count


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 5))
