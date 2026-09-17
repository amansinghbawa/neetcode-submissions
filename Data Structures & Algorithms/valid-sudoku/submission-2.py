from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        if not self.check_columns():
            return False
        if not self.check_rows():
            return False
        if not self.check_subboxes():
            return False
        return True

    def check_columns(self):
        #print("check_columns")
        for row_index in range(9):
            nums = []
            for column_index in range(9):
                nums.append(self.board[column_index][row_index])
            if self.is_duplicate_number(nums):
                #print("row_index", row_index)
                return False
        return True

    def check_rows(self):
        #print("check_rows")
        for column_index in range(9):
            nums = []
            for row_index in range(9):
                nums.append(self.board[column_index] [row_index])
            if self.is_duplicate_number(nums):
                #print("column_index", column_index)
                return False
        return True

    def check_subboxes(self):
        """
        0,0   0,3   0,6
        3,0   3,3   3,6
        6,0   6,3   6,6
        """
        #print("check_subboxes")
        for row_index in range(0,7,3):
            for column_index in range(0,7,3):
                nums = []
                for i in range(row_index, row_index+3):
                    for j in range(column_index, column_index+3):
                        nums.append(self.board[i ][j])
                if self.is_duplicate_number(nums):
                    #print("column_index", column_index, "row_index", row_index)
                    return False
        return True


    def is_duplicate_number(self, nums):
        row = []
        for num in nums:
            if num not in row or num == ".":
                row.append(num)
            else:
                #print(num)
                return True
        return False