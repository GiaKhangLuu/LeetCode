import json
import time
import math
import timeout_decorator

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    
    @timeout_decorator.timeout(1)
    def myPow(self, x, n):
        if n == 0:
            return 1

        if n == 1:
            return x

        is_negative = n < 0
        n = abs(n)
        n_half = int(n / 2)

        rs = self.myPow(x, n_half)

        is_odd = n % 2 != 0
        rs = rs * rs * x if is_odd else rs * rs
        rs = 1 / rs if is_negative else rs

        return rs


    def test(self, func, inp, expectation):
        x, n = list(inp.values())
        out = func(x, n)
        out = round(out, 5)
        expectation = round(expectation, 5)
             
        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

"""
def run_test_cases(data_file='./data.json'):
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(inp))
        solution.test(solution.myPow, inp, expectation)
"""

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(inp))
        solution.test(solution.myPow, inp, expectation)
"""
    # Creating a Process
    action_process = Process(target=run_test_cases)

    # Starting the process and blocking for 5 seconds
    action_process.start()
    action_process.join(timeout=5)

    # Terminating the process
    print('{}Timeout{}'.format(color_code['red'], color_code['end']))
"""
