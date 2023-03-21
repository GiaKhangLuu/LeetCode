import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def countAndSay(self, n):
        if n == 1:
            return "1"

        cnt_and_say = self.countAndSay(n - 1)

        # Add '0' to the first and the last of cnt_and_say. Then starting to compare
        # Ex: cnt_and_say = '111221' -> '01112210'
        # Compare: '0111221' & '1112210'
        comparision_str = '0' + cnt_and_say + '0'
        same_digits = []
        for x, y in zip(comparision_str[:-1], comparision_str[1:]):
            if x != y:
                same_digits += y
            else:
                same_digits[-1] += y
        same_digits = same_digits[:-1]  # removing last element

        # COUNT
        say = []
        for digits in same_digits:
            count = len(digits)
            if count == 1:
                say.append("1{}".format(digits[-1]))
            else:
                say.append("{}{}".format(count, digits[-1]))

        return "".join(say)


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
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(inp))
        solution.test(solution.countAndSay, inp, expectation)


