import json
from typing import List

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num, count = 0, 0
        for num in nums:
            if count == 0:
                majority_num = num
            if majority_num == num:
                count += 1
            else:
                count -= 1
        return majority_num

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
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.majorityElement, inp, expectation)