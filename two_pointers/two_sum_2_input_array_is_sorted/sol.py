import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

    def test(self, func, inp, expectation):
        nums, target = inp['numbers'], inp['target']
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
        solution.test(solution.twoSum, inp, expectation)


