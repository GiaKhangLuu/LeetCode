import json
import time
import math
import numpy as np

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def permuteUnique(self, nums):
        decision_dict = {}  
        for num in nums:
            if num in decision_dict:
                decision_dict[num] += 1
            else:
                decision_dict[num] = 1

        def dfs(decision_dict):
            rs = []
            if len(decision_dict) == 1:
                first_key = next(iter(decision_dict))
                first_value = decision_dict[first_key]
                return [[first_key] * first_value]
            
            for value in decision_dict.keys():
                sub_dict = decision_dict.copy()
                sub_dict[value] = sub_dict[value] - 1
                if not sub_dict[value]:
                    sub_dict.pop(value)

                groups = dfs(sub_dict)
                for group in groups:
                    group.append(value)
                rs.extend(groups)
                
            return rs
        return dfs(decision_dict)   

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

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(inp))
        solution.test(solution.permuteUnique, inp, expectation)


