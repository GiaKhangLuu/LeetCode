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
    def buildTree(self, preorder, inorder):
        if not (preorder and inorder):
            return None
        
        value = preorder[0]
        node = TreeNode(val=value)
        node_index_in_inorder = inorder.index(value)
        node.left = self.buildTree(preorder[1:node_index_in_inorder + 1],
                                   inorder[:node_index_in_inorder])
        node.right = self.buildTree(preorder[node_index_in_inorder + 1:],
                                    inorder[node_index_in_inorder + 1:])

        return node

    def test(self, func, inp, expectation):
        preorder, inorder = inp['preorder'], inp['inorder']

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

        expected_node = create_tree(expectation, 0)
        out_node = func(preorder, inorder)
        
        def check(out_node, expected_node):
            if out_node and expected_node:
                if out_node.val != expected_node.val:
                    return False
                return (check(out_node.left, expected_node.left) &
                        check(out_node.right, expected_node.right))
            else:
                return True

        if check(out_node, expected_node):
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_construct_bt_from_pre_and_in_traversal.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.buildTree, inp, expectation)