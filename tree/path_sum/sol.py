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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if (root.val == targetSum and
            root.left is None and
            root.right is None):
            return True
        target_of_child = targetSum - root.val
        left_result = self.hasPathSum(root.left, target_of_child)
        right_result = self.hasPathSum(root.right, target_of_child)
        result = left_result or right_result
        return result

    def test(self, func, inp, expectation):
        nodes, targetSum = inp['root'], inp['targetSum']

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
        out = func(head, targetSum)

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
        solution.test(solution.hasPathSum, inp, expectation)
