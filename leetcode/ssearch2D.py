class Solution:
    def searchMatrix(self, matrix: list[list], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True

        return False
