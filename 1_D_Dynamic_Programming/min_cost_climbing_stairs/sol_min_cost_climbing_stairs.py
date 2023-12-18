import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def minCostClimbingStairs(self, cost):
        min_cost_each_stair = [-1] * len(cost)
        def climb(n):
            if n == 1:
                return 0
            if n == 2:
                return min(cost[0], cost[1])
            if min_cost_each_stair[n - 1] != -1:
                return min_cost_each_stair[n - 1]
            cost_one_step_before = climb(n - 1) + cost[n - 1]
            cost_two_steps_before = climb(n - 2) + cost[n - 2]
            min_cost = min(cost_one_step_before, cost_two_steps_before)
            min_cost_each_stair[n - 1] = min_cost
            return min_cost
        return climb(len(cost))

    def test(self, func, inp, expectation):
        cost = inp['cost']
        rs = func(cost)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_min_cost_climbing_stairs.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.minCostClimbingStairs, inp, expectation)