import json
import time
import math
from typing import List

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        left = 0
        right = left + 1
        rs = []
        while right < len(nums):
            if nums[right] > nums[right - 1] + 1:
                if nums[left] == nums[right - 1]:
                    rs.append("{}".format(nums[left]))
                else:
                    rs.append("{}->{}".format(nums[left], nums[right - 1]))
                left = right
            right += 1
        if nums[left] == nums[right - 1]:
            rs.append("{}".format(nums[left]))
        else:
            rs.append("{}->{}".format(nums[left], nums[right - 1]))

        return rs

    def test(self, func, inp, expectation):
        nums = inp["nums"]
        out = func(nums)

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
        solution.test(solution.summaryRanges, inp, expectation)


