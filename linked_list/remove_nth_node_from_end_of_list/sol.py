import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time: {:.5f}ms'.format((end - start)*1000))
    return wrapper

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd(self, head, n):
        dummy_node = ListNode(val=0, next=head)
        left = right = dummy_node
        distance = 0
        while right.next != None:
            right = right.next
            distance += 1
            if distance > n:
                left = left.next
                distance -= 1
        left.next = left.next.next
        return dummy_node.next

    @time_func 
    def test(self, func, head, n, expectation):
        list_ele = head
        head = curr_node = ListNode(list_ele[0])
        for ele in list_ele[1:]:
            node = ListNode(ele)
            curr_node.next = node
            curr_node = node

        out = func(head, n)
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
        head, n = inp['head'], inp['n']
        #solution.removeNthFromEnd(head, n)

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.removeNthFromEnd, head, n, expectation)