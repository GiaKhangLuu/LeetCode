import json
import time

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def removeElement(self, nums, val):
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)

    def test(self, func, inp, expectation):
        inp_nums, val = list(inp.values())
        k, out_nums = list(expectation.values())
        out = func(inp_nums, val)
        print(inp_nums)

        assert out == k, '{}Wrong{}'.format(color_code['red'], color_code['end'])

        for i in range(k):
            try:
                inp_nums.index(out_nums[i])
            except:
                print('{}Wrong{}'.format(color_code['red'], color_code['end']))

        print('{}Correct{}'.format(color_code['green'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case {} <<<<<<<<<<'.format(inp))
        solution.test(solution.removeElement, inp, expectation)
