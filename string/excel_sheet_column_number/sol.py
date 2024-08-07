import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        scale = len(columnTitle) - 1
        for char in columnTitle:
            index = ord(char) - ord("A") + 1
            result += index * (26 ** scale)
            scale -= 1
        return result

    def test(self, func, inp, expectation):
        columnTitle = inp["columnTitle"]
        out = func(columnTitle)

        if out == expectation:
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

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.titleToNumber, inp, expectation)