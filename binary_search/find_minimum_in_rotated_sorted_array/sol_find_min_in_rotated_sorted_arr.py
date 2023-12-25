import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def findMin(self, nums):
        min_num = 5001
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[l] and nums[m] <= nums[r]:
                min_num = min(nums[m], min_num)
                r = m - 1
            else:
                if nums[m] >= nums[l]:
                    if nums[m] < nums[r]:
                        r = m - 1
                    else:
                        l = m + 1

        return min_num
       

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
    file_test_case = open('./data_find_min_in_rotated_sorted_arr.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.findMin, inp, expectation)