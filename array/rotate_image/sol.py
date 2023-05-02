import json
import time
import math
import numpy as np

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def replace(self, matrix, mover, new_pos, rotated_mask):
        for value, pos in zip(mover, new_pos):
            row, col = pos
            if rotated_mask[row][col] != True:
                matrix[row][col] = value
                rotated_mask[row][col] = True
        return matrix, rotated_mask

    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        # Do not create rotated_masks like this:
        # -> rotated_masks = [[False] * n] * n
        # Because this statement copies the pointer of the first row
        # then expand to next row. Therefore, modifying any row that 
        # will affect to other rows

        # -> Do this instead 
        rotated_masks = [[False] * n for _ in range(n)]
        row, start, end = 0, 0, n
        
        while start < (end - 1):
            mover = matrix[row][start:end]

            # Retrieving old pos and calculating new pos by formula:
            # new_col = n - old_row - 1, n = len(matrix) -> n - row - 1
            # new_row = old_col
            # Ex: [0, 1] -> [1, 2]
            old_pos = [(row, j) for j in range(start, end)]
            new_pos = [(col, n - row - 1) for row, col in old_pos]  

            new_pos_masks = [rotated_masks[row][col] for row, col in new_pos]
            flag = sum(new_pos_masks)

            # If all values in new pos has rotated -> stop
            while flag < len(new_pos):
                # Saving all values in new pos
                saver = [matrix[row][col] for row, col in new_pos]

                # Replacing
                matrix, rotated_masks = self.replace(matrix, mover, new_pos, rotated_masks)

                mover = saver
                old_pos = new_pos
                new_pos = [(col, n - row - 1) for row, col in old_pos]
                new_pos_masks = [rotated_masks[row][col] for row, col in new_pos]
                flag = sum(new_pos_masks)
        
            row += 1
            start += 1
            end -= 1

    def test(self, func, inp, expectation):
        func(inp)

        if inp == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(inp))
        solution.test(solution.rotate, inp, expectation)

