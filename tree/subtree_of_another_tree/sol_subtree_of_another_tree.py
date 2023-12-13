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
    def is_same_tree(self, node_1, node_2):
        if node_1 == node_2 == None:
            return True
        if node_1 and node_2 and node_1.val == node_2.val:
            return (self.is_same_tree(node_1.left, node_2.left) and 
                    self.is_same_tree(node_1.right, node_2.right))
        return False

    def isSubtree_clean_version(self, root, subRoot):
        if not root or not subRoot:
            return False
        if self.is_same_tree(root, subRoot):
            return True
        return (self.isSubtree_clean_version(root.left, subRoot) or
                self.isSubtree_clean_version(root.right, subRoot))

    def isSubtree_messy_version(self, root, subRoot):
        def is_same_tree(node_1, node_2):
            if node_1 == node_2 == None:
                return True
            if (node_1 == None) or (node_2 == None):
                return False
            if node_1.val == node_2.val:
                rs = True
            else:
                rs = False
            return rs and is_same_tree(node_1.left, node_2.left) and is_same_tree(node_1.right, node_2.right)

        stored_nodes = []
        def traverse(node):
            if not node:
                return 
            if node.val == subRoot.val:
                stored_nodes.append(node)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        
        for node in stored_nodes:
            if is_same_tree(node, subRoot):
                return True
        return False

    def test(self, func, inp, expectation):
        nodes, sub_nodes = inp['root'], inp['subRoot']

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
        root, subRoot = create_tree(nodes, 0), create_tree(sub_nodes, 0)

        out = func(root, subRoot)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
        

if __name__ == '__main__':
    file_test_case = open('./data_subtree_of_another_tree.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        
        # Version 1: Messy version
        #solution.test(solution.isSubtree_messy_version, inp, expectation)

        # Version 2: Clean version
        solution.test(solution.isSubtree_clean_version, inp, expectation)
