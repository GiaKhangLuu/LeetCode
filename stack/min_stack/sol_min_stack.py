import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    class MinStack:
        def __init__(self):
            self.min_vals = []
            self.stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            if not len(self.min_vals) or self.min_vals[-1] >= val:
                self.min_vals.append(val)
            
        def pop(self) -> None:
            last_val = self.stack[-1]
            self.stack = self.stack[:-1]
            if last_val == self.min_vals[-1]:
                self.min_vals = self.min_vals[:-1]

        def top(self) -> int:
            return self.stack[-1]
            
        def getMin(self) -> int:
            return self.min_vals[-1]
                                                    
    def test(self, inp, expectation):
        commands, args = inp['commands'], inp['args']
        result_list = []
        for command, argument in zip(commands, args):
            if command == 'MinStack':
                obj = self.MinStack()
                result_list.append(None)
            elif command == 'push':
                obj.push(argument[0])
                result_list.append(None)
            elif command == 'pop':
                obj.pop()
                result_list.append(None)
            elif command == 'top':
                top_value = obj.top()
                result_list.append(top_value)
            else:
                min_value = obj.getMin()
                result_list.append(min_value)

        if result_list == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result_list, color_code['end']))
            
if __name__ == '__main__':
    file_test_case = open('./data_min_stack.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)

