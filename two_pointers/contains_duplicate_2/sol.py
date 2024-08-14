import json
import time
import math
from typing import List

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = min(k, len(nums) - 1)
        while left != right:
            if nums[left] in nums[left + 1:right + 1]:
                return True
            left += 1
            right = min(right + 1, len(nums) - 1)
        return False

    def test(self, func, inp, expectation):
        nums, k = inp["nums"], inp["k"]
        out = func(nums, k)

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
        solution.test(solution.containsNearbyDuplicate, inp, expectation)


