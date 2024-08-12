import json
import time
import math
from typing import Optional

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        fake_node = ListNode(-1, head)
        pre, curr = fake_node, fake_node.next
        while curr:
            if curr.val == val:
                pre.next = curr.next
                curr = curr.next
            else:
                pre = curr
                curr = curr.next
        
        return fake_node.next

    def test(self, func, inp, expectation):
        head, val = inp['head'], inp["val"]
        list_ele = head
        if len(list_ele):
            head = curr_node = ListNode(list_ele[0])
            for ele in list_ele[1:]:
                node = ListNode(ele)
                curr_node.next = node
                curr_node = node
        else:
            head = None

        out = func(head, val)
        rs = [] 
        while out:
            rs.append(out.val)
            out = out.next
        if rs == expectation:
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
        solution.test(solution.removeElements, inp, expectation)