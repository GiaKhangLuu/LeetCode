import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def maxArea(self, height):
        l, r = 0, len(height) - 1
        calc_area = lambda i, j: min(height[i], height[j]) * (j - i)
        max_area = calc_area(l, r)

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(calc_area(l, r), max_area)
        
        return max_area

    def test(self, func, inp, expectation):
        out = func(inp)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.maxArea, inp, expectation)


