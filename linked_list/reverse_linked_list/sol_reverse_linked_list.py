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
    def reverseList_iteration(self, head):
        initial_head = head
        while initial_head and initial_head.next:
            curr = initial_head.next
            initial_head.next = curr.next
            curr.next = head
            head = curr
        
        return head

    def reverseList_recursion(self, head):
        def reverse(initial_head, head):
            if initial_head and initial_head.next:
                curr = initial_head.next
                initial_head.next = curr.next
                curr.next = head
                head = curr
                head = reverse(initial_head, head)

            return head
        
        return reverse(head, head)

    def test(self, func, inp, expectation):
        head = inp['head']
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
    file_test_case = open('./data_reverse_linked_list.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        # Method 1: Recursion Approach
        #solution.test(solution.reverseList_recursion, inp, expectation)

        # Method 2: Iteration Approach
        solution.test(solution.reverseList_iteration, inp, expectation)