import json
import time
import numpy as np

def time_func(func):
    def wrapper(*args, **kargs):
        start = time.time()
        rs = func(*args, **kargs)
        end = time.time()
        print('Time: {:.5f}ms'.format((end - start)*1000))
        return rs
    return wrapper

class Test:
    
    @time_func
    def verifyAnswer(self, expected, output):
        for ele in expected:
            if not ele in output:
                return False
        return True 

class Solution:

    def letterCombinations(self, digits):
        digit_letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not len(digits):
            return []
        if len(digits) == 1:
            return digit_letter_dict[digits]

        letters = [digit_letter_dict[digit] for digit in digits]
        letters = np.meshgrid(*letters)
        letter_combinations = letters[0]
        for letter in letters[1:]:
            letter_combinations = np.char.add(letter_combinations, letter)
        letter_combinations = letter_combinations.flatten().tolist()
        return letter_combinations

##################################################
# Test 
##################################################

file_test_case = open('./data.json')
test_case = json.load(file_test_case)

for i in range(len(test_case)):
    digits, expected = list(test_case[i].values())

    output = Solution().letterCombinations(digits)
    result = Test().verifyAnswer(expected, output)
    color = '\033[92m' if result else '\033[31m'

    print('----------- Test case ', i + 1, '---------------')
    print('>>>>>>>>>>> Result: {}{}{}'.format(color, result, '\033[0m'))
