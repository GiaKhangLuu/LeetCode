import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        rs = ""

        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0
            add_all = digit_a + digit_b + carry
            rs = str(add_all % 2) + rs
            carry = add_all // 2

        if carry == 1:
            return "1" + rs
        return rs

    def test(self, func, inp, expectation):
        a, b = inp["a"], inp["b"]
        out = func(a, b)

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
        solution.test(solution.addBinary, inp, expectation)