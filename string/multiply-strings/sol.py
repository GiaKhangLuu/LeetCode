import time
import json


class Test:

    def verifyAnswer(self, expected, output):
        return True if expected == output else False

class Solution:

    def multiply(self, num1, num2):
        x = y = 0
        for string_digit in num1:
            int_digit = ord(string_digit) - ord("0")
            x = x * 10 + int_digit
        for string_digit in num2:
            int_digit = ord(string_digit) - ord("0")
            y = y * 10 + int_digit
        return str(x * y)


##################################################
# Test 
##################################################

file_test_case = open('./data.json')
test_case = json.load(file_test_case)

for i in range(len(test_case)):
    inp, expected = list(test_case[i].values())
    num1 = inp["num1"]
    num2 = inp["num2"]
    
    output = Solution().multiply(num1, num2)
    result = Test().verifyAnswer(expected, output)
    color = '\033[92m' if result else '\033[31m'


    print('----------- Test case ', i + 1, '---------------')
    print('>>>>>>>>>>> Output ', output)
    print('>>>>>>>>>>> Expected ', expected)
    print('>>>>>>>>>>> Result: {}{}{}'.format(color, result, '\033[0m'))
