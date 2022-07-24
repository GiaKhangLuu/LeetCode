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
    
        result = node = ListNode()
        for i in range(len(nums)):
            node.val = nums[i]
            if i != len(nums) - 1:
                node.next = ListNode()
                node = node.next
        
        return result

    def verifyListNode(self, l1, l2):

        while(l1 or l2):
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next

        return True

        

# Definition for solution     
class Solution:

    def addTwoNumbers(self, l1, l2):
        
        result = node = ListNode()
        residual = 0

        while(l1 or 
                l2 or 
                residual != 0):
            
            node.next = ListNode()
            node = node.next

            l1_digit = l1.val if l1 else 0
            l2_digit = l2.val if l2 else 0

            total = l1_digit + l2_digit + residual

            # Ex: 19 % 10 = 9, this value will be appended directly to the result
            next_digit = total % 10  
            # Ex: 19 // 10 = 1, this value will be added to the next sum
            residual = total // 10

            node.val = next_digit

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

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
    result = Solution().addTwoNumbers(l1, l2)
    end = time.time()

    print('>>>>>>>>>>> Test case ', i + 1)
    print('>>>>>>>>>>> Result: ', 
            Test().verifyListNode(result, output))
    print('>>>>>>>>>>> Total time: {} ms'.format(round(end - start, 4)))

    
