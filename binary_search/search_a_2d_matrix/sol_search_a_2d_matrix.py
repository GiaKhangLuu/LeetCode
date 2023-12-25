import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def searchMatrix(self, matrix, target):
        def binary_search(target_row=None):
            l = 0
            r = len(matrix[target_row]) - 1 if target_row is not None else len(matrix) - 1
            while l <= r:
                m = (l + r) // 2
                if target_row is not None:
                    start_num = end_num = matrix[target_row][m]
                else:
                    start_num, end_num = matrix[m][0], matrix[m][-1]
                if start_num <= target <= end_num:
                    return m
                elif target > start_num:
                    l = m + 1
                else:
                    r = m - 1
            return -1 

        target_row_idx = binary_search()
        if target_row_idx != -1:
            return True if binary_search(target_row_idx) != -1 else False

        return False


    def test(self, func, inp, expectation):
        matrix, target = inp["matrix"], inp['target']
        result = func(matrix, target)

        if result == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_search_a_2d_matrix.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.searchMatrix, inp, expectation)