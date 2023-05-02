import json
import time

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSymmetric(self, root, d=None, stage=0):

        if d == None:
            d = dict()

        value = None if root == None else root.val

        if stage not in d:
            d.update({ stage: [value] })
        else:
            d[stage].append(value)

        if root == None:
            return

        next_stage = stage + 1
        self.isSymmetric(root.left, d, next_stage)
        self.isSymmetric(root.right, d, next_stage)

        if stage == 0:
            d[stage].append(value)
            print(d)
            for stage_values in d.values():
                middle = len(stage_values) // 2
                half_left, half_right = stage_values[:middle], stage_values[middle:]
                half_right.reverse()
                if half_left != half_right:
                    return False
            return True


    def create_tree(self, inp, i = -1):
         if i < len(inp) - 1:
             i += 1
         else:
             return None, inp, i
         val = inp[i]
         if val:
             n = TreeNode(val)
             n.left, inp, i = self.create_tree(inp, i)
             n.right, inp, i = self.create_tree(inp, i)
             return n, inp, i
         else:
             return None, inp, i

    def test(self, func, inp, expectation):

        root, _, _ = self.create_tree(inp)

        out = func(root)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))


if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case {} <<<<<<<<<<'.format(inp))
        solution.test(solution.isSymmetric, inp, expectation)

