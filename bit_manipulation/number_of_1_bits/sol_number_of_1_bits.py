import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            cnt += 1 if n & 1 == 1 else 0
            n >>= 1
        return cnt

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
    file_test_case = open('./data_number_of_1_bits.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.hammingWeight, inp, expectation)