import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

# Definition for singly-linked list.
class Node:
    def __init__(self, x=0, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        ori_nodes = []
        copied_nodes = []
        node = head
        
        def travel(node):
            if not node:
                return None
            copied_node = Node(x=node.val)
            ori_nodes.append(node)
            copied_nodes.append(copied_node)
            copied_node.next = travel(node.next)
            copied_node.random = copied_nodes[ori_nodes.index(node.random)] if node.random else None
            return copied_node

        head = travel(node)
        return head

    def test(self, func, inp, expectation):
        # Creating linked list input
        head = inp['head']
        list_ele = head
        nodes = []
        if len(list_ele):
            head = curr_node = Node(list_ele[0][0])
            nodes.append(head)
            for ele in list_ele[1:]:
                node = Node(ele[0])
                nodes.append(node)
                curr_node.next = node
                curr_node = node
        else:
            head = None
        # Add random node in input
        curr = head
        for ele in list_ele:
            random_index = ele[-1]
            if random_index is not None:
                curr.random = nodes[random_index]
            curr = curr.next

        # Create list of output 
        out = func(head)
        rs = [] 
        output_nodes = []
        while out:
            rs.append([out.val])
            output_nodes.append(out)
            out = out.next
        for i, output_node in enumerate(output_nodes):
            random_node = output_node.random
            if random_node:
                rs[i].append(output_nodes.index(random_node))
            else:
                rs[i].append(None)

        # Checking
        if rs == expectation:
            for node in output_nodes:
                if node.next in nodes or node.random in nodes:
                    print('{}Wrong: node(s) in copied list is linked to node(s) in original list{}'.format(color_code['red'], color_code['end']))       
                    return
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_copy_list_with_random_pointer.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        solution.test(solution.copyRandomList, inp, expectation)