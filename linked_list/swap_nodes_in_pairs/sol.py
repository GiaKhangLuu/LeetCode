import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs(self, head):
        fake_head = ListNode(next=head)
        pre_node, curr_node = fake_head, head

        while curr_node and curr_node.next:
            next_node = curr_node.next
            
            pre_node.next = next_node
            curr_node.next = next_node.next
            next_node.next = curr_node

            pre_node = curr_node
            curr_node = pre_node.next

        return fake_head.next

    def test(self, func, head, expectation):
        list_ele = head
        if len(list_ele):
            head = curr_node = ListNode(list_ele[0])
            for ele in list_ele[1:]:
                node = ListNode(ele)
                curr_node.next = node
                curr_node = node
        else:
            head = None

        out = func(head)
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
        solution.test(solution.swapPairs, inp, expectation)