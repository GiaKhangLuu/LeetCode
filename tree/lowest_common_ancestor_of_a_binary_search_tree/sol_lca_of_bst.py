import json
from re import sub

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
    def lowestCommonAncestor(self, root, p, q):
        def find_lca(start_node):
            if (start_node.val < p.val and
                start_node.val < q.val):
                return find_lca(start_node.right)
            if (start_node.val > p.val and
                start_node.val > q.val):
                return find_lca(start_node.left)
            return start_node

        return find_lca(root)

    def test(self, func, inp, expectation):
        nodes, p, q = inp['root'], inp['p'], inp['q']

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
        p, q = TreeNode(val=p), TreeNode(val=q)

        out = func(root, p, q)

        if out.val == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
        

if __name__ == '__main__':
    file_test_case = open('./data_lca_of_bst.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        
        solution.test(solution.lowestCommonAncestor, inp, expectation)