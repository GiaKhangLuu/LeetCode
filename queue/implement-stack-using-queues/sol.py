import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    class MyStack:

        def __init__(self):
            self.main_queue, self.assistant_queue = [], []

        def push(self, x):
           self.main_queue.append(x) 
           return None

        def dequeue(self):
            dequeue_value = None
            if len(self.main_queue) > 0:
                dequeue_value = self.main_queue[0]
                self.main_queue.remove(self.main_queue[0])
            return dequeue_value

        def swap(self):
            temp = self.assistant_queue
            self.assistant_queue = self.main_queue
            self.main_queue = temp

        def pop(self):
            rs = None
            # dequeue until we meet the last value
            for i in range(len(self.main_queue)):
                if len(self.main_queue) == 1:
                    rs = self.dequeue()
                else:
                    # add value to assistant_queue
                    self.assistant_queue.append(self.dequeue())

            # swap these two queues
            #self.debug()
            self.swap()
            #self.debug()
            return rs

        def debug(self):
            print("Main queue: ", self.main_queue)
            print("Assistant queue: ", self.assistant_queue)
             
        def top(self):
            return self.main_queue[len(self.main_queue) - 1] if len(self.main_queue) > 0 else None

        def empty(self):
            return True if len(self.main_queue) == 0 else False

    def test(self, inp, expectation):

        commands, values = inp[0], inp[1]
        obj = None
        rs = []

        for cmd, val in zip(commands, values):
            if cmd == "MyStack":
               obj = self.MyStack() 
               rs.append(None)
            if cmd == "push":
                obj.push(val[0])
                rs.append(None)
            if cmd == "pop":
                rs.append(obj.pop())
            if cmd == "top":
                rs.append(obj.top())
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

