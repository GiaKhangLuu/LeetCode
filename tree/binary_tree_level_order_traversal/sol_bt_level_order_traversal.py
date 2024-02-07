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

    # Method 01
    def levelOrder_BFS(self, root):
        queue = collections.deque()
        queue.append(root)
        rs = []

        while queue:
            nodes_in_depth = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    nodes_in_depth.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if nodes_in_depth:
                rs.append(nodes_in_depth)

        return rs

    # Method 02
    def levelOrder_recursion(self, root):
        depth = 0
        rs = []

        def traverse(node, depth):
            if node:
                if len(rs) > depth:
                    rs[depth].append(node.val)
                else:
                    rs.append([node.val])
                traverse(node.left, depth + 1)
                traverse(node.right, depth + 1)

        traverse(root, depth)

        return rs

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
        
if __name__ == '__main__':
    file_test_case = open('./data_bt_level_order_traversal.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        # Recursion 
        #solution.test(solution.levelOrder_recursion, inp, expectation)

        # BFS 
        solution.test(solution.levelOrder_BFS, inp, expectation)