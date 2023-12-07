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
    def hasCycle_floyd(self, head):
        tortoise, hare = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
            
        return False

    def hasCycle_iteration(self, head):
        nodes = []
        curr = head
        while curr:
            if curr in nodes:
                return True
            nodes.append(curr)
            curr = curr.next

        return False

    def test(self, func, inp, expectation):
        head, pos = inp['head'], inp['pos']
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
        
        if len(nodes) and pos != -1:
            nodes[-1].next = nodes[pos]

        out = func(head)
        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_linked_list_cycle.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        # Approach 01: Iteration method
        #solution.test(solution.hasCycle_iteration, inp, expectation)

        # Approach 02: Floyd's tortoise and hare
        solution.test(solution.hasCycle_floyd, inp, expectation)
