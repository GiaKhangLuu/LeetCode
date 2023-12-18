import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    # Bottom_up approach
    def climbStairs_bottom_up(self, n):
        if n == 1:
            return 1
        ways = [0] * len(range(n))
        ways[0], ways[1] = 1, 2
        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[-1]

    # Memoization approach
    def climbStairs_memoization(self, n):
        memo = [0] * len(range(n))
        def climb(n):
            if memo[n - 1] != 0:
                return memo[n - 1]
            if n == 2:
                memo[1] = 2
                return memo[1]
            if n == 1:
                memo[0] = 1
                return memo[0]
            count_way = climb(n - 1)
            count_way += climb(n - 2)
            memo[n - 1] = count_way
            return count_way
        return climb(n)

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
    file_test_case = open('./data_climbing_stairs.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        # Approach 01: Memoization approach
        #solution.test(solution.climbStairs_memoization, inp, expectation)

        # Approach 02: Bottom-up approach
        solution.test(solution.climbStairs_bottom_up, inp, expectation)
