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

    def postorderTraversal(self, root, rs=None):
        if rs == None:
            rs = []
        if root:
            self.postorderTraversal(root.left, rs)
            self.postorderTraversal(root.right, rs)
            rs.append(root.val)
        return rs

    def test(self, func, inp, expectation):

        def create_tree(inp, i):
            if i < len(inp) - 1:
                i += 1
            else:
                return None, inp, i
            val = inp[i]
            if val:
                n = TreeNode(val)
                n.left, inp, i = create_tree(inp, i)
                n.right, inp, i = create_tree(inp, i)
                return n, inp, i
            else:
                return None, inp, i
        
        root, _, _ = create_tree(inp, -1)

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
        solution.test(solution.postorderTraversal, inp, expectation)
