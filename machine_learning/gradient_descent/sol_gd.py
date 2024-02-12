import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def get_minimizer(self, iterations, learning_rate, init):
        rs = init
        for i in range(iterations):
            rs -= learning_rate * 2 * rs

        return round(rs, 5)

    def test(self, func, inp, expectation):
        iterations, learning_rate, init = inp["iterations"], inp["learning_rate"], inp["init"]

        out = func(iterations, learning_rate, init)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)

if __name__ == '__main__':
    file_test_case = open('./data_gd.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.get_minimizer, inp, expectation)