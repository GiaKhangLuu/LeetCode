import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        # 1. Find the middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle_node = slow
        head_second = middle_node.next
        middle_node.next = None

        if head_second:
            # 2. Reverse the second half
            prev_node, curr = head_second, head_second.next
            while curr:
                curr_next = curr.next
                curr.next = head_second
                prev_node.next = curr_next
                head_second = curr
                curr = curr_next

            # 3. Merge element-wise
            curr_first_half, curr_second_half = head, head_second
            while curr_first_half and curr_second_half:
                next_first_half = curr_first_half.next
                next_second_half = curr_second_half.next
                curr_first_half.next = curr_second_half
                curr_second_half.next = next_first_half
                curr_first_half, curr_second_half = next_first_half, next_second_half

        return head

    def test(self, func, inp, expectation):
        head = inp['head']
        list_ele = head
        nodes = []
        if len(list_ele):
            head = curr_node = ListNode(list_ele[0])
            nodes.append(head)
            for ele in list_ele[1:]:
                node = ListNode(ele)
                nodes.append(node)
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
    file_test_case = open('./data_reorder_list.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        solution.test(solution.reorderList, inp, expectation)