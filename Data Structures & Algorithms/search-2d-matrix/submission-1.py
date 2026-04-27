class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            center = (left + right) //2
            if matrix[center][0] == target:
                return True
            elif matrix[center][0] < target:
                left = center + 1
            else:
                right = center - 1
        left2, right2 = 0, len(matrix[0]) - 1
        while left2 <= right2:
            center = (left2 + right2) //2
            if matrix[right][center] == target:
                return True
            elif matrix[right][center] < target:
                left2 = center + 1
            else:
                right2 = center - 1
        return False
