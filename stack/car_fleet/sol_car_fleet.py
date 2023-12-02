import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def carFleet_stack(self, target, position, speed):
        """
        This is stack approach 
        """
        pos_and_speed = [(pos, spd) for pos, spd in zip(position, speed)]
        pos_and_speed = sorted(pos_and_speed)[::-1]
        stack = []

        for pos, spd in pos_and_speed:
            reaching_des_time = (target - pos) / spd
            stack.append(reaching_des_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

    def carFleet_two_pointers(self, target, position, speed):
        """
        This is two_pointers approach 
        """
        car_fleets = 0
        sorted_pos_spd = list(zip(position, speed))
        sorted_pos_spd = sorted(sorted_pos_spd, key=lambda x: x[0], reverse=True)
        reaching_des_time = [(target - pos) / spd for pos, spd in sorted_pos_spd]
        ahead = 0
        
        while ahead < len(position):
            below = ahead + 1
            while below < len(position) and reaching_des_time[below] <= reaching_des_time[ahead]:
                below += 1
            ahead = below
            car_fleets += 1

        return car_fleets

    def test(self, func, inp, expectation):
        target, position, speed = inp['target'], inp['position'], inp['speed']
        result = func(target, position, speed)

        if result == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_car_fleet.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        #solution.test(solution.carFleet_two_pointers, inp, expectation)
        solution.test(solution.carFleet_stack, inp, expectation)