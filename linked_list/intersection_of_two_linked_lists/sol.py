import json
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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a, len_b = 0, 0
        curr_a, curr_b = headA, headB
        while curr_a:
            curr_a = curr_a.next
            len_a += 1
        while curr_b:
            curr_b = curr_b.next
            len_b += 1

        curr_a, curr_b = headA, headB
        a_remain, b_remain = len_a, len_b
        while curr_a and curr_b:
            if curr_a == curr_b:
                return curr_a
            if a_remain > b_remain:
                curr_a = curr_a.next
                a_remain -= 1
            elif b_remain > a_remain:
                curr_b = curr_b.next
                b_remain -= 1
            else:
                curr_a = curr_a.next
                curr_b = curr_b.next
                a_remain -= 1
                b_remain -= 1

        return None

    def test(self, func, inp, expectation):
        intersect_value = inp['intersectVal']
        listA = inp['listA']
        listB = inp['listB']
        skipA = inp['skipA']
        skipB = inp['skipB']

        previous_node_a = ListNode()
        for i, x in enumerate(listA):
            if i == skipA:
                break
            node = ListNode(val=x)
            if i == 0:
                head_a = node
            previous_node_a.next = node
            previous_node_a = previous_node_a.next

        previous_node_b = ListNode()
        for i, x in enumerate(listB):
            if i == skipB:
                break
            node = ListNode(val=x)
            if i == 0:
                head_b = node
            previous_node_b.next = node
            previous_node_b = previous_node_b.next

        for i in range(skipA, len(listA)):
            node = ListNode(listA[i])
            previous_node_a.next = node
            previous_node_b.next = node
            previous_node_a = previous_node_a.next
            previous_node_b = previous_node_b.next


        out = func(head_a, head_b)

        if expectation:
            if out and out.val == expectation:
                print('{}Correct{}'.format(color_code['green'], color_code['end']))
            else:
                print('{}Wrong{}'.format(color_code['red'], color_code['end']))
        else:
            if out is not None:
                print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            else:
                print('{}Correct{}'.format(color_code['green'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        # Approach 02: Floyd's tortoise and hare
        solution.test(solution.getIntersectionNode, inp, expectation)
