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
    def diameterOfBinaryTree(self, root):
        def traverse(node, diameter=0):
            if not node:
                return 0, diameter
            depth_left, diameter = traverse(node.left, diameter)
            depth_right, diameter = traverse(node.right, diameter)
            diameter = max(diameter, depth_left + depth_right)
            return (max(depth_left, depth_right) + 1, diameter)
            
        _, diameter = traverse(root)
        return diameter

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

        out = func(head)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_diameter_of_binary_tree.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.diameterOfBinaryTree, inp, expectation)
