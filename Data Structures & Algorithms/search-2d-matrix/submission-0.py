class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # --- STEP 1: Binary Search to find the correct ROW (O(log m)) ---
        
        row_start, row_end = 0, m - 1
        target_row = -1
        
        while row_start <= row_end:
            mid = (row_start + row_end) // 2
            
            # If the target is found at the start of the row, return True
            if matrix[mid][0] == target:
                return True
            
            # If target is greater than the row's start, it MIGHT be in this row or below
            elif matrix[mid][0] < target:
                target_row = mid # This is a potential candidate row
                row_start = mid + 1
            
            # If target is less than the row's start, it's in a row above
            else:
                row_end = mid - 1

        # Check for invalid cases: target is smaller than the smallest element
        if target_row == -1:
             return False # The loop found no row where target >= matrix[row][0]

        # --- STEP 2: Binary Search the identified ROW (O(log n)) ---
        
        row = matrix[target_row]
        col_start, col_end = 0, n - 1
        
        while col_start <= col_end:
            mid = (col_start + col_end) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                col_start = mid + 1
            else:
                col_end = mid - 1
                
        return False