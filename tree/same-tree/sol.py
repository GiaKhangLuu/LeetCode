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

    def isSameTree(self, p, q):

        # Check p and q == None (end of node)
        if p == q == None:
            return True

        # Either p is end or q end
        if (p == None) or (q == None):
            return False

        rs = (p.val == q.val)
        left_rs = self.isSameTree(p.left, q.left)
        right_rs = self.isSameTree(p.right, q.right)

        return rs and left_rs and right_rs

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

        p, q = list(inp.values())

        
        root_p, _, _ = self.create_tree(p)
        root_q, _, _ = self.create_tree(q)

        out = func(root_p, root_q)

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
        solution.test(solution.isSameTree, inp, expectation)
