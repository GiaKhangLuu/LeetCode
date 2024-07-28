import json
import math
from typing import List

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num_replacements = len(nums1) - m
        nums1[m:m+num_replacements] = nums2        

        left, right = 0, m
        while left < right and right < len(nums1):
            a, b = nums1[left], nums1[right]
            if a > b:
                temp = b
                nums1[left+1:right+1] = nums1[left:right] 
                nums1[left] = b
                right += 1
            left += 1

    def test(self, func, inp, expectation):
        nums1, m, nums2, n = inp['nums1'], inp["m"], inp["nums2"], inp["n"]
        func(nums1, m, nums2, n)

        if nums1 == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.merge, inp, expectation)