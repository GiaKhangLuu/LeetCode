import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def isPalindrome(self, s):
        def check_digit_or_char(x):
            if (ord(x) in range(ord('a'), ord('z') + 1) or
                ord(x) in range(ord('0'), ord('9') + 1)):
                    return True
            return False

        l, r = 0, len(s) - 1
        while l < r:
            left_char, right_char = s[l].lower(), s[r].lower()
            if not check_digit_or_char(left_char):
                l += 1
                continue
            if not check_digit_or_char(right_char):
                r -= 1
                continue
            if left_char != right_char:
                return False
            l += 1
            r -= 1

        return True

    def test(self, func, inp, expectation):
        out = func(inp)

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
        solution.test(solution.isPalindrome, inp, expectation)


