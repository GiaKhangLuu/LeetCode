import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    """
    Approach 01: Bit Manipulation 
    """
    def missingNumber_bit_manipulation(self, nums):
        rs = 0
        for i in range(len(nums) + 1):
            rs ^= i
        for num in nums:
            rs ^= num
        return rs
    
    """
    Approach 02: Math 
    """
    def missingNumber_math(self, nums):
        return sum(range(len(nums) + 1)) - sum(nums)

    def test(self, func, inp, expectation):
        nums = inp['nums']
        rs = func(nums)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_missing_number.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        
        # Approach 01: Bit Manipulation
        #solution.test(solution.missingNumber_bit_manipulation, inp, expectation)

        # Approach 02: Math
        solution.test(solution.missingNumber_math, inp, expectation)