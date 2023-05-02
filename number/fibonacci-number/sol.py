import json
import time

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def fibo_for(self, n):
        left, right = 0, 1

        if n == 0: 
            return left

        if n == 1:
            return right

        for i in range(n - 1):
            temp = right
            right = left + right
            left = temp

        return right

    def fibo_recursive(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.fibo_recursive(n - 1) + self.fibo_recursive(n - 2)


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

        print('>>>>>>>>>>> Test case <<<<<<<<<<', i + 1)
        solution.test(solution.fibo_recursive, inp, expectation)

