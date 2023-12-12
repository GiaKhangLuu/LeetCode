import json
from itertools import chain

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def traverse(node):
            is_balanced = False
            if not node:
                return 0, True
            left_depth, balanced_left = traverse(node.left)
            right_depth, balanced_right = traverse(node.right)

            if abs(left_depth - right_depth) <= 1:
                is_balanced = True
            is_balanced = balanced_left and balanced_right and is_balanced
            depth = max(left_depth, right_depth) + 1

            return depth, is_balanced
        
        _, is_balanced = traverse(root)
        return is_balanced

    def test(self, func, inp, expectation):
        nodes = inp['root']
        
        def create_tree(depth):
            if depth >= len(nodes):
                return None
            node_value = nodes[depth]
            if node_value is None:
                return None
            node = TreeNode(val=node_value)
            node.left = create_tree(depth * 2 + 1)
            node.right = create_tree(depth * 2 + 2)
            return node
        head = create_tree(0)

        out = func(head)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_balanced_binary_tree.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.isBalanced, inp, expectation)
