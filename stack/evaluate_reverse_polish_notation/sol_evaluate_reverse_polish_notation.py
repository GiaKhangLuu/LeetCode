import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def evalRPN(self, tokens):
        stack = []

        for tok in tokens:
            if tok == '+':
                stack.append(stack.pop() + stack.pop())
            elif tok == '-':
                subtrahend = stack.pop()
                minuend = stack.pop()
                stack.append(minuend - subtrahend)
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(dividend / divisor))
            else:
                stack.append(int(tok))

        return stack[0]

    def test(self, func, inp, expectation):
        tokens = inp['tokens']
        result = func(tokens)

        if result == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_eval_reverse_polish_notation.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.evalRPN, inp, expectation)