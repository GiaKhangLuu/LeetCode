import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def generateParenthesis(self, n):
        # Adding "(" if open_cnt < n
        # Adding ")" if close_cnt < open
        # Valid parenthesis if open_cnt = close_cnt = n

        stack = []
        rs = []

        def backtracking(open_cnt, close_cnt):
            if open_cnt == close_cnt == n:
                rs.append("".join(stack))
                return

            if open_cnt < n:
                stack.append("(")
                backtracking(open_cnt + 1, close_cnt)
                # The stack is global. So, we have to remove "(" or ")" to
                # make the stack is consistent for the next possible recursions.
                stack.pop()

            if close_cnt < open_cnt:
                stack.append(")")
                backtracking(open_cnt, close_cnt + 1)
                stack.pop()

        backtracking(0, 0)
        return rs

    def test(self, func, inp, expectation):
        out = func(inp)

        cnt = 0
        for parenthesis in expectation:
            if parenthesis in out:
                cnt += 1
            else:
                print('{}Wrong{}'.format(color_code['red'], color_code['end']))
                print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
                print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))
                break
             
        if cnt == len(expectation):
            print('{}Correct{}'.format(color_code['green'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i))
        solution.test(solution.generateParenthesis, inp, expectation)


