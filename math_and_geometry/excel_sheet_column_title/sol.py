import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        rs = ""
        while columnNumber != 0:
            char_index = (columnNumber - 1) % 26
            rs = chr(char_index + ord("A")) + rs
            columnNumber = (columnNumber - 1) // 26

        return rs

    def test(self, func, inp, expectation):
        columnNumber = inp['columnNumber']
        rs = func(columnNumber)

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
        solution.test(solution.convertToTitle, inp, expectation)