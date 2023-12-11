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
    def invertTree(self, root):
        def dfs(node):
            if not node:
                return None
            node_left = dfs(node.left)
            node_right = dfs(node.right)
            node.left, node.right = node_right, node_left
            return node

        return dfs(root)

    def test(self, func, inp, expectation):
        nodes = inp['root']
    
        def create_tree(depth):
            if depth >= len(nodes):
                return None
            node_value = nodes[depth]
            node = TreeNode(val=node_value)
            node.left = create_tree(depth * 2 + 1)
            node.right = create_tree(depth * 2 + 2)
            return node
        head = create_tree(0)
        
        tree_dict = dict()
        def get_tree_values(node, depth):
            if not node:
                return
            if depth in tree_dict:
                tree_dict[depth].append(node.val)
            else:
                tree_dict[depth] = [node.val]
            get_tree_values(node.left, depth+1)
            get_tree_values(node.right, depth+1)
        
        out = func(head)
        get_tree_values(out, 0)
        out_values = list(chain.from_iterable(list(tree_dict.values())))
            
        if out_values == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_invert_binary_tree.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.invertTree, inp, expectation)
