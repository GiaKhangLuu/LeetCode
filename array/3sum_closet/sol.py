import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        closest = max_int = 2 ** 64 - 1
        rs = None
        for pivot in range(len(nums)):
            l, r = pivot + 1, len(nums) - 1
            while l < r:
                three_sum = nums[pivot] + nums[l] + nums[r]
                diff = three_sum - target

                rs = three_sum if abs(diff) < closest else rs
                closest = abs(diff) if abs(diff) < closest else closest
                
                if diff > 0:
                    r = r - 1
                else:
                    l = l + 1

        return rs

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

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.threeSumClosest, inp, expectation)


