import json
from typing import List, Optional
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None

        mid = (len(nums) - 1) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node 

    def test(self, func, inp, expectation):
        nums = inp['nums']
        root = func(nums)
        results = []

        tree_dict = dict()
        def get_tree_values(node, depth):
            if not node:
                if depth in tree_dict:
                    tree_dict[depth].append(None)
                else:
                    tree_dict[depth] = [None]
                return
            if depth in tree_dict:
                tree_dict[depth].append(node.val)
            else:
                tree_dict[depth] = [node.val]
            get_tree_values(node.left, depth+1)
            get_tree_values(node.right, depth+1)
        
        get_tree_values(root, 0)

        remove_keys = []
        for i in tree_dict.keys():
            cnt = 0
            for vl in tree_dict[i]:
                cnt += 1 if vl is None else 0
            if cnt == len(tree_dict[i]):
                remove_keys.append(i) 
        for key in remove_keys:
            tree_dict.pop(key)

        out_values = list(chain.from_iterable(list(tree_dict.values())))

        if out_values == expectation:
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
        solution.test(solution.sortedArrayToBST, inp, expectation)
