import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def longestCommonPrefix(self, strs):
        prefix_length = 0
        rs = ""
        strs_len = len(strs)

        if strs_len == 0 or strs_len == 1:
            return ""

        base = strs[0]
        prefix = "".join([base[i] for i in range(prefix_length + 1)])

        while prefix_length != base:
            for idx in range(1, strs_len):
                word = strs[idx]
                char_list = word.split(prefix)
    
                if char_list[0] != "":
                    return rs
    
                if idx == (strs_len - 1):
                    rs = prefix
                    prefix_length += 1
                    prefix = "".join([base[i] for i in range(prefix_length + 1)])

        return base

    def test(self, func, inp, expectation):
        out = func(inp)
             
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
        solution.test(solution.longestCommonPrefix, inp, expectation)


