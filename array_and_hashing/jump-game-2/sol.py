import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def jump(self, nums):
        cnt = 0
        destination = len(nums) - 1
        num_positions = list(range(len(nums)))

        current_jumps = [nums[0]]
        current_positions = [0]

        while destination not in current_positions:
            max_jump = 0
            for pos, curr in zip(current_positions, current_jumps):
                jump = pos + curr
                max_jump = jump if jump > max_jump else max_jump
            current_positions = num_positions[current_positions[-1] + 1:max_jump+1]
            current_jumps = [nums[pos] for pos in current_positions]
            cnt += 1
                
        return cnt

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
        solution.test(solution.jump, inp, expectation)


