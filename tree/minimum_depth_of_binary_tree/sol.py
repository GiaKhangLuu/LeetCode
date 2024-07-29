import json
from typing import Optional

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1
        return min(left_depth, right_depth) + 1

    def test(self, func, inp, expectation):
        nodes = inp['root']

        def create_tree(depth, is_left_null=False):
            if depth >= len(nodes):
                return None
            node_value = nodes[depth]
            if node_value is None:
                return None
            node = TreeNode(val=node_value)
            if is_left_null:
                node_left = create_tree(depth + 1)
                node.left = node_left
                node.right = create_tree(depth + 2, node_left == None)
            else:
                node_left = create_tree(depth * 2 + 1) 
                node.left = node_left
                node.right = create_tree(depth * 2 + 2, node_left == None)
            return node
        head = create_tree(0)
        out = func(head)

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

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.minDepth, inp, expectation)
