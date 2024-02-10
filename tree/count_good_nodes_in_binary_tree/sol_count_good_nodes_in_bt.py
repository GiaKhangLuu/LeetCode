import json
import collections

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
    def goodNodes(self, root):
        MIN_VALUE = -(10 ** 4 + 1)

        def dfs(node, max_value_in_path):
            if not node:
                return 0

            rs = left_cnt = right_cnt = 0
            if node.val >= max_value_in_path:
                rs = 1
                max_value_in_path = node.val            
            left_cnt = dfs(node.left, max_value_in_path)
            right_cnt = dfs(node.right, max_value_in_path)
            
            return rs + left_cnt + right_cnt
                
        cnt = dfs(root, MIN_VALUE)

        return cnt

    def test(self, func, inp, expectation):
        nodes = inp['root']

        def create_tree(nodes, depth):
            if depth >= len(nodes):
                return None
            node_value = nodes[depth]
            if node_value is None:
                return None
            node = TreeNode(val=node_value)
            node.left = create_tree(nodes, depth * 2 + 1)
            node.right = create_tree(nodes, depth * 2 + 2)
            return node

        root = create_tree(nodes, 0)

        out = func(root)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)

if __name__ == '__main__':
    file_test_case = open('./data_count_good_nodes_in_bt.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.goodNodes, inp, expectation)