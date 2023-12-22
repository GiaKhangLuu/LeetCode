import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def isHappy(self, n):
        def sum_of_squares_of_digits(n):
            rs = 0
            while n != 0:
                last_digit = n % 10
                rs += last_digit ** 2
                n //= 10
            return rs
        
        tortoise = sum_of_squares_of_digits(n)
        rabit = sum_of_squares_of_digits(sum_of_squares_of_digits(n))
        while tortoise != rabit:
            tortoise = sum_of_squares_of_digits(tortoise)
            rabit = sum_of_squares_of_digits(sum_of_squares_of_digits(rabit))
        return True if tortoise == rabit == 1 else False


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
    file_test_case = open('./data_happy_number.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.isHappy, inp, expectation)