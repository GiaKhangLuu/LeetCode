import json
import time

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def removeElement(self, nums, val):
        pos_dict = dict()
    
        # 1. Creating position dictionary
        for i in range(len(nums)):
            list_keys = list(pos_dict.keys())
            
            if nums[i] not in list_keys:
                pos_dict.update({ nums[i]: [i] })
            else:
                pos_dict[nums[i]].append(i)

        if val not in pos_dict:
            return len(nums)

        # 2. Cal. k 
        k = len(nums) - len(pos_dict[val])

        # 3. Swap
        pos_vals = pos_dict[val]
        count = 0 
        for pos_val in pos_vals:
            if pos_val >= k:
                continue
            while nums[pos_val] == val:
                nums[pos_val] = nums[k + count]
                count += 1

        return k

    def test(self, func, inp, expectation):
        inp_nums, val = list(inp.values())
        k, out_nums = list(expectation.values())
        out = func(inp_nums, val)
        print(inp_nums)

        assert out == k, '{}Wrong{}'.format(color_code['red'], color_code['end'])

        for i in range(k):
            try:
                inp_nums.index(out_nums[i])
            except:
                print('{}Wrong{}'.format(color_code['red'], color_code['end']))

        print('{}Correct{}'.format(color_code['green'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case {} <<<<<<<<<<'.format(inp))
        solution.test(solution.removeElement, inp, expectation)
