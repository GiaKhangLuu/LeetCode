import json

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

    def isValidBST(self, root):
        
        def dfs(node, lower_lim, upper_lim):
            if node:
                if not (lower_lim < node.val & node.val < upper_lim):
                    return False
                return (dfs(node.left, lower_lim, node.val) & 
                        dfs(node.right, node.val, upper_lim))
            return True

        lower_lim, upper_lim = float("-inf"), float("inf")
        return dfs(root, lower_lim, upper_lim)

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
    file_test_case = open('./data_validate_bst.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.isValidBST, inp, expectation)