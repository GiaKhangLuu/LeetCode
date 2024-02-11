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

    def kthSmallest_optimized(self, root, k):
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val 
            cur = cur.right
    
    def kthSmallest_O_n(self, root, k):
        my_stack, result_list = [], []

        def dfs(node):
            if node:
                my_stack.append(node.val)
                dfs(node.left)
                result_list.append(my_stack.pop())
                dfs(node.right)
        dfs(root)
        
        return result_list[k - 1]

    def test(self, func, inp, expectation):
        nodes, k = inp['root'], inp['k']

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

        out = func(root, k)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)

if __name__ == '__main__':
    file_test_case = open('./data_kth_smallest_ele_in_a_bst.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.kthSmallest_O_n, inp, expectation)
        #solution.test(solution.kthSmallest_optimized, inp, expectation)