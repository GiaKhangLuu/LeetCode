import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def traverse(n):
            if n == 1:
                return True
            if n <= 0:
                return False
            if n % 2 == 0:
                rs = True
            else:
                rs = False
            return rs and traverse(n / 2)
        return traverse(n)

    def test(self, func, inp, expectation):
        n = inp['n']
        rs = func(n)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.isPowerOfTwo, inp, expectation)