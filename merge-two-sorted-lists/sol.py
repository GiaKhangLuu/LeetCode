import json
import time

# Definition for List-Node
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for testing
class Test:

    def createListNode(self, nums):

        if len(nums) == 0:
            return None

        listNode = node = ListNode()
        for i in range(len(nums)):
            node.val = nums[i]
            if i != len(nums) - 1:
                node.next = ListNode()
                node = node.next

        return listNode

    def verifyListNode(self, l1, l2):

        while(l1 or l2):
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next

        return True

# Definition for solution
class Solution:

    def mergeTwoLists(self, list1, list2):

        result = node = ListNode()
        queue = list()
        # According to the constraint: -100 <= Node.val <= 100, so that
        # we can use block_value = 999
        block_value = 999

        while (list1 or list2):

            list1_digit = list1.val if list1 else block_value
            list2_digit = list2.val if list2 else block_value

            if list2_digit < list1_digit:
                # Make sure that list1_digit always less than list2_digit
                list1_digit, list2_digit = list2_digit, list1_digit

            while (len(queue) > 0) and (queue[0] <= list1_digit):
                node.next = ListNode(queue.pop(0)) 
                node = node.next
            
            # Two input lists are sorted lists, so that at least 1 digit in 
            # the current loop bigger than any digits stored in queue
            if list2_digit != block_value:
                queue.append(list2_digit) 
            node.next = ListNode(list1_digit)              
            node = node.next
           
            # Set value for the next loop
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        while (len(queue) > 0) and (queue[0] != block_value):
            node.next = ListNode(queue.pop(0))
            node = node.next
            
        return result.next
            

##################################################
# Test 
##################################################

file_test_case = open('./data.json')
test_case = json.load(file_test_case)

for i in range(len(test_case)):
    input, output = list(test_case[i].values())
    l1, l2 = list(input.values())
    l1 = Test().createListNode(l1)
    l2 = Test().createListNode(l2)
    output = Test().createListNode(output)
    
    start = time.time()
    result = Solution().mergeTwoLists(l1, l2)
    end = time.time()

    print('>>>>>>>>>>> Test case ', i + 1)
    print('>>>>>>>>>>> Result: ', 
            Test().verifyListNode(result, output))
    print('>>>>>>>>>>> Total time: {} ms'.format(round(end - start, 4)))

