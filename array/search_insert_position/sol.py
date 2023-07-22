import json
import time

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def searchInsert(self, nums, target):
        if (len(nums) == 0) or (target < nums[0]):
            return 0
        if target > nums[-1]:
            return len(nums)
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            curr_num = nums[mid]
            if curr_num == target:
                return mid
            if curr_num < target:
                left = mid + 1
                if target <= nums[left]:
                    return left
            else:
                right = mid - 1
                if target > nums[right]:
                    return mid

    def test(self, func, inp, expectation):
        nums, target = inp['nums'], inp['target']
        out = func(nums, target)

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
        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i))
        solution.test(solution.searchInsert, inp, expectation)


