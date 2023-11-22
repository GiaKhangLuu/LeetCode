import json
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def minEatingSpeed(self, piles, h):
        efficient_speed = max(piles)
        lower_lim, upper_lim = 1, efficient_speed
        
        while lower_lim <= upper_lim:
            eating_speed = (lower_lim + upper_lim) // 2
            total_hour = sum([math.ceil(pile / eating_speed) for pile in piles])
            
            if total_hour > h:
                lower_lim = eating_speed + 1
            elif total_hour <= h:
                upper_lim = eating_speed - 1
                efficient_speed = min(eating_speed, efficient_speed)

        return efficient_speed

    def test(self, func, inp, expectation):
        piles, h = inp['piles'], inp['h']
        out = func(piles, h)
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
        solution.test(solution.minEatingSpeed, inp, expectation)


