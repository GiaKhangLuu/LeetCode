import json
import time
import math
import numpy as np

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def groupAnagrams(self, strs, index=0, list_encode=None, result=None):
        if result == None and list_encode == None:
            result = []
            list_encode = []

        if index == len(strs):
            return result

        word = strs[index]

        character_list = [0] * 26 # 26 is num of characters (a -> z)
        first_position = ord('a')

        for char in word:
            position = ord(char) - first_position
            character_list[position] += 1

        same_encode_index = -1
        for i, encode in enumerate(list_encode):
            if encode == character_list:
                same_encode_index = i
                result[same_encode_index].append(word)
                break

        if same_encode_index == -1:
            list_encode.append(character_list)
            result.append([word])                

        result = self.groupAnagrams(strs, index+1, list_encode, result)

        return result

    def test(self, func, inp, expectation):
        out = func(inp)

        out_pos, exp_pos = [], []

        for group in out:
            out_pos.append([inp.index(word) for word in group])

        for group in expectation:
            exp_pos.append([inp.index(word) for word in group])

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
        solution.test(solution.groupAnagrams, inp, expectation)
