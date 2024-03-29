import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def intToRoman(self, num):

        values = [1, 5, 10, 50, 100, 500, 1000]
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        rs = ''
        elements = []
        symbol_elements = []
        remainder = num

        while remainder != 0:
            digit_count = len(str(remainder))
            divisor = int('1' + ((digit_count - 1) * '0'))
            ele = math.floor(remainder / divisor) * divisor
            elements.append(ele)
            remainder = remainder % divisor

            symbol_ele = ''  

            # Borrowing
            clone_values = values.copy()
            clone_values.insert(0, 0)
            for value in clone_values:
                temp = ele
                temp += value
                if temp in values:
                    symbol_ele = symbols[values.index(temp)]
                    if value != 0:
                        symbol_borrowing = symbols[values.index(value)]
                        symbol_ele = "".join([symbol_borrowing, symbol_ele])
                    symbol_elements.append(symbol_ele)
                    break

            if symbol_ele != '':
                continue
            
            # Dividing
            divident = ele
            for value in values[::-1]:
                temp = divident % value
                if temp != divident:
                    quotient = math.floor(divident / value)
                    divident = temp
                    symbol_ele += quotient * symbols[values.index(value)]

            symbol_elements.append(symbol_ele)
        rs = "".join(symbol_elements)
        return rs


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
        solution.test(solution.intToRoman, inp, expectation)


