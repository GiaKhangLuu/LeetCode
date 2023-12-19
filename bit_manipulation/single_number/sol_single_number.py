import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def singleNumber(self, nums):
        rs = 0
        for num in nums:
            rs ^= num
        return rs

    def test(self, func, inp, expectation):
        nums = inp['nums']
        rs = func(nums)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_single_number.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.singleNumber, inp, expectation)