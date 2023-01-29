import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

#    def intToRoman(self, num):
#        
#        values = [1, 5, 10, 50, 100, 500, 1000]
#        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
#
#        rs = ''
#        quotient = 0
#
#        while num != 0: 
#            print(num)
#
#            # Borrowing
#            if num in values:
#                rs += symbols[values.index(num)]
#                return rs
#
#            for value in values[::-1]:
#                temp = num
#                temp += value
#
#                if temp in values:
#                    rs += symbols[values.index(temp)]
#                    symbol = symbols[values.index(value)]
#                    rs = "".join([symbol, rs])
#
#                    return rs
#
#            # Dividing
#            for divisor in values[::-1]:
#                temp = num % divisor
#                if temp != num:
#                    quotient = math.floor(num / divisor)
#                    num = temp
#                    rs += quotient * symbols[values.index(divisor)]
#
#                    break
#
#
##        if quotient != 1:
##            rs += (quotient - 1) * 'I'
#
#        return rs

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
            elements.append(math.floor(remainder / divisor) * divisor)
            remainder = remainder % divisor

        for ele in elements:
            symbol_ele = ''
            # Borrowing
            if ele in values:
                symbol_ele += symbols[values.index(ele)]
                symbol_elements.append(symbol_ele)
                continue

            for value in values[::-1]:
                temp = ele
                temp += value

                if temp in values:
                    symbol_ele += symbols[values.index(temp)]
                    symbol_borrowing = symbols[values.index(value)]
                    symbol_ele = "".join([symbol_borrowing, symbol_ele])
                    symbol_elements.append(symbol_ele)
                    continue
                
            if symbol_ele != '':               
                continue

            # Dividing
            num = ele
            for divisor in values[::-1]:
                temp = num % divisor
                if temp != num:
                    quotient = math.floor(num / divisor)
                    num = temp
                    symbol_ele += quotient * symbols[values.index(divisor)]

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


