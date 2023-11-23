import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def searchRange(self, nums, target):
        def bin_search(is_find_left_most):
            partition, l, r = -1, 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    partition = m
                    if is_find_left_most:
                        r = m - 1
                    else:
                        l = m + 1
            
            return partition
            
        left_pos, right_pos = bin_search(True), bin_search(False)
        return [left_pos, right_pos]

    def test(self, func, inp, expectation):
        nums, target = inp['nums'], inp['target']
        out = func(nums, target)
        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.searchRange, inp, expectation)