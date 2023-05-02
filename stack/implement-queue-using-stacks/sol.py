import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    class MyQueue:

        def __init__(self):
            self.main_stack, self.assistant_stack = [], []
            self.length = 0

        def push(self, x):
            self.main_stack.append(x)
            self.length += 1
            self.debug('push')
            return None

        def comeback(self):
            while len(self.assistant_stack) > 0:
                self.main_stack.append(self.assistant_stack.pop())

        def pop(self):
            self.length -= 1
            for i in range(self.length):
                value = self.main_stack.pop()
                self.assistant_stack.append(value)
            last_value = self.main_stack.pop()

            self.comeback()
            self.debug('pop')

            return last_value
        
        def peek(self):
            return self.main_stack[0]

        def empty(self):
            return True if self.length == 0 else False

        def debug(self, func_type):
            print(func_type)
            print("Main stack: ", self.main_stack)
            print("Assistant stack: ", self.assistant_stack)

    def test(self, inp, expectation):

        commands, values = inp[0], inp[1]
        obj = None
        rs = []

        for cmd, val in zip(commands, values):
            if cmd == "MyQueue":
               obj = self.MyQueue() 
               rs.append(None)
            if cmd == "push":
                obj.push(val[0])
                rs.append(None)
            if cmd == "pop":
                rs.append(obj.pop())
            if cmd == "peek":
                rs.append(obj.peek())
            if cmd == "empty":
                rs.append(obj.empty())

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

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i))
        solution.test(inp, expectation)

