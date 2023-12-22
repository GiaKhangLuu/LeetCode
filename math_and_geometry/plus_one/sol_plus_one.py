import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def plusOne(self, digits):
        add_one, i = True, -1
        while i >= -len(digits) and add_one:
            digit = digits[i]
            new_digit = digit + 1
            add_one = True if new_digit == 10 else False
            digits[i] = 0 if new_digit == 10 else new_digit
            i -=1
        if add_one:
            digits.insert(0, 1)
        return digits

    def test(self, func, inp, expectation):
        digits = inp['digits']
        rs = func(digits)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_plus_one.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.plusOne, inp, expectation)