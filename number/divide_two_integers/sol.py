import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def divide(self, dividend, divisor):
        min_vl = -2 ** 31
        max_vl = 2**31 - 1

        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        remainers = abs_dividend
        quotient = 0

        while remainers >= abs_divisor:
            temp = abs_divisor
            count = 0

            while temp <= remainers:
                count += 1 if count == 0 else count
                temp += temp

            quotient += count
            remainers -= temp // 2 

        quotient = -quotient if abs_dividend != dividend else quotient
        quotient = -quotient if abs_divisor != divisor else quotient

        return max(min_vl, quotient) if quotient < 0 else min(max_vl, quotient)

    def test(self, func, inp, expectation):
        dividend, divisor = inp["dividend"], inp["divisor"]
        out = func(dividend, divisor)
             
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
        solution.test(solution.divide, inp, expectation)


