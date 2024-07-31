import json
from typing import List

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rs = []
        def generate_row(row_th, container):
            if row_th == 1:
                container.append([1])
            else:
                previous_rows = generate_row(row_th - 1, container)
                last_row = previous_rows[-1]
                new_row = []
                for i in range(1, row_th - 1):
                    new_row.append(last_row[i-1] + last_row[i])
                new_row.append(1)  # add last 1
                new_row.insert(0, 1)  # add first 1
                container.append(new_row)
            return container                
        
        rs = generate_row(numRows, rs)
        return rs

    def test(self, func, inp, expectation):
        numRows = inp["numRows"]
        rs = func(numRows)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.generate, inp, expectation)