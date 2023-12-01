import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = [0]
        i = 1
        
        while i < len(temperatures):
            next_tem = temperatures[i]
            current_tem = temperatures[stack[-1]]
            while next_tem > current_tem:
                current_idx = stack.pop()
                answer[current_idx] = i - current_idx
                
                if not len(stack):
                    break
                else:
                    current_tem = temperatures[stack[-1]]

            stack.append(i)
            i += 1

        return answer

    def test(self, func, inp, expectation):
        temperatures = inp['temperatures']
        result = func(temperatures)

        if result == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_daily_temperatures.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.dailyTemperatures, inp, expectation)