import json
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def productExceptSelf(self, nums):
        hash_map = dict()
        rs = [0] * len(nums)
        
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        for i, num in enumerate(nums):
            num_clone = hash_map.copy()
            num_clone[num] -= 1
            values = list(num_clone.keys())
            freqs = list(num_clone.values())
            eles = [val ** freq for val, freq in zip(values, freqs)]
            rs[i] = math.prod(eles)

        return rs

    def test(self, func, inp, expectation):
        nums = inp['nums']
        out = func(nums)

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

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.productExceptSelf, inp, expectation)