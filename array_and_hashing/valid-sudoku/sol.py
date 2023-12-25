import json
import time
import math
import numpy as np
import collections

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution_By_Khang:
    """
    This naive solution does not occure at the same loop.
    """

    def isRepetition(self, arr):
        check_list = list(map(lambda i: arr[i] == arr[i + 1], range(len(arr) - 1)))
        rs = sum(check_list)
        return False if rs == 0 else True
        

    def checkRow(self, board):
        processed_board = board.copy()
        n_rows, _ = processed_board.shape

        for i in range(n_rows):
            row = processed_board[i, :].ravel()

            # Remove "." from array
            row = np.delete(row, np.where(row == "."))

            row.sort()
            
            rs = self.isRepetition(row)

            if rs:
                return False
        return True

    def checkCol(self, board):
        processed_board = board.copy()
        _, n_cols = processed_board.shape

        for i in range(n_cols):
            col = processed_board[:, i].ravel()

            # Remove "." from array
            col = np.delete(col, np.where(col == "."))

            col.sort()

            rs = self.isRepetition(col)

            if rs:
                return False
        return True

    def checkSubBoxes(self, board):
        proc_board = board.copy()
        n_rows, n_cols = proc_board.shape

        for i in range(0, n_rows, 3):
            for j in range(0, n_cols, 3):
                sub_boxes = proc_board[i:i+3, j:j+3].ravel()
                # Remove "." from array
                sub_boxes = np.delete(sub_boxes, np.where(sub_boxes == "."))

                sub_boxes.sort()
                rs = self.isRepetition(sub_boxes)

                if rs:
                    return False
        return True


    def isValidSudoku(self, board):
        board = np.array(board)
        rs_1 = self.checkRow(board)
        rs_2 = self.checkCol(board)
        rs_3 = self.checkSubBoxes(board)
        return rs_1 and rs_2 and rs_3

    def test(self, func, inp, expectation):
        out = func(inp)
             
        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

class Solution_By_NeetCode:

    def isValidSudoku(self, board):
        row_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        subbox_map = collections.defaultdict(set)
        
        # The board has shape 9x9
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                big_box_row, big_box_col = i // 3, j // 3
                if value == '.':
                    continue
                if (value in row_map[i] or
                   value in col_map[j] or
                   value in subbox_map[(big_box_row, big_box_col)]):
                       return False
                row_map[i].add(value)
                col_map[j].add(value)
                subbox_map[(big_box_row, big_box_col)].add(value)
        return True

    def test(self, func, inp, expectation):
        out = func(inp)
             
        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))
    

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    #solution_by_khang = Solution_By_Khang()
    solution_by_neetcode = Solution_By_NeetCode()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i))
        #solution_by_khang.test(solution_by_khang.isValidSudoku, inp, expectation)
        solution_by_neetcode.test(solution_by_neetcode.isValidSudoku,
                                  inp, expectation)


