import time
import json

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time: {:.5f}ms'.format((end - start)*1000))
    return wrapper

class Test:

    @time_func
    def verifyAnswer(self, expected, output):
        rs =  True if expected == output else False
        color = '\033[92m' if rs else '\033[31m'
        print('>>>>>>>>>>> Output ', output)
        print('>>>>>>>>>>> Expected ', expected)
        print('>>>>>>>>>>> Result: {}{}{}'.format(color, rs, '\033[0m'))

class Solution:

    def strStr(self, haystack, needle):
        len_needle = len(needle)
        len_haystack = len(haystack)

        if len_haystack == len_needle == 0:
            return 0
        if len_haystack < len_needle:
            return -1
        
        start, end = 0, len_needle
        substr = haystack[start:end]

        while substr != needle:
            start += 1
            end += 1
            if end > len_haystack + 2:
                return -1
            substr = haystack[start:end]

        return start

##################################################
# Test 
##################################################

file_test_case = open('./data.json')
test_case = json.load(file_test_case)

for i in range(len(test_case)):
    inp, expected = list(test_case[i].values())
    haystack = inp["haystack"]
    needle = inp["needle"]
    
    print('----------- Test case ', i + 1, '---------------')
    output = Solution().strStr(haystack, needle)
    Test().verifyAnswer(expected, output)


