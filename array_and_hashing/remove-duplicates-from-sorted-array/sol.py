import json
import time

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    
    def removeDuplicates_khang_code(self, inp):
        l, k = 0, 1

        for r in range(1, len(inp)):
            if inp[r] != inp[l]:
                l += 1
                k += 1
                inp[l] = inp[r]
        return k

    def removeDuplicates_neetcode(self, inp):
        l = 1

        for r in range(1, len(inp)):
            if inp[r] != inp[r - 1]:
                inp[l] = inp[r]
                l += 1

        return l

    def check_ref(self, inp):
        inp.append(10)

    def test(self, func, inp, expectation):
        out = func(inp)
        print(inp)
        k, nums = list(expectation.values())
        assert out == k, '{}Wrong{}'.format(color_code['red'], color_code['end'])
        for i in range(k):
            assert inp[i] == nums[i], '{}Wrong{}'.format(color_code['red'], color_code['end'])
        print('{}Correct{}'.format(color_code['green'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case {} <<<<<<<<<<'.format(inp))
        solution.test(solution.removeDuplicates_khang_code, inp, expectation)
