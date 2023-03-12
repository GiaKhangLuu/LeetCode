import json
import time
import math
import numpy as np

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def permute(self, nums):
        """
        Neet code
        """
        rs = []

        if len(nums) == 1:
            return [nums.copy()]

        for remove_num in nums:
            temp_nums = nums.copy()
            temp_nums.remove(remove_num)

            groups = self.permute(temp_nums)

            for group in groups:
                group.append(remove_num)
            rs.extend(groups)

        return rs

        """ My code

        ---> Conclusion: It is not necessarily true that passing 
        result through the next call. This result list just need
        to extend the return from its descendants.

        if rs == None:
            rs = []

        if len(nums) == 1:
            return [nums]

        for remove_nums in nums:
            temp_nums = nums.copy()
            temp_nums.remove(remove_nums)
            groups = self.permute(temp_nums, rs)

            for x in groups:
                x.append(remove_nums)

        """


    def test(self, func, inp, expectation):
        out = func(inp)

        if len(out) == len(expectation):
            for permute_out in out:
                try:
                    expectation.index(permute_out)
                except:
                    print('{}Wrong{}'.format(color_code['red'], color_code['end']))
    
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
             
#        if out == expectation:
#            print('{}Correct{}'.format(color_code['green'], color_code['end']))
#        else:
#            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
#            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
#            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(inp))
        solution.test(solution.permute, inp, expectation)


