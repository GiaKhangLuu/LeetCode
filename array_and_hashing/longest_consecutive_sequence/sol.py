import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def longestConsecutive(self, nums):
        if not len(nums):
            return 0
        longest_consecutive = 1
        
        nums = sorted(nums)
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    streak += 1
                else:
                    longest_consecutive = max(longest_consecutive, streak)
                    streak = 1
            
        longest_consecutive = max(longest_consecutive, streak)

        return longest_consecutive


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
        solution.test(solution.longestConsecutive, inp, expectation)


