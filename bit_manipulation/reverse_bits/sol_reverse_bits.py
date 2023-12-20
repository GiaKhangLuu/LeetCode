import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def reverseBits_neet_code(self, n):
        rs = 0
        for i in range(32):
            bits = (n >> i) & 1
            rs |= bits << (31 - i)
        return rs

    def reverseBits_khang_code(self, n):
        s = ''
        while n != 0:
            s += str(n & 1)
            n >>= 1
        s += '0' * (32 - len(s))
        rs = int(s, 2)
        return rs

    def test(self, func, inp, expectation):
        n = inp['n']
        n = int(n, 2)
        rs = func(n)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_reverse_bits.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        # Approach 01: Khang version
        #solution.test(solution.reverseBits_khang_code, inp, expectation)

        # Approach 02: Neetcode version
        solution.test(solution.reverseBits_neet_code, inp, expectation)