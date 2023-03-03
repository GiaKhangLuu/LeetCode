import json
import time
import math
import numpy as np

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def threeSum(self, nums):
        rs = []

        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            # Skip to the next value if the current value equal the previous one
            # Duplicate value causes duplicate triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:

                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    rs.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip to the next value until current left are not equal the previous one
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return rs

    def test(self, func, inp, expectation):
        out = func(inp)

        expectation = np.array(expectation).reshape(-1).tolist()
        out = np.array(out).reshape(-1).tolist()
        expectation.sort()
        out.sort()
             
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
        solution.test(solution.threeSum, inp, expectation)


