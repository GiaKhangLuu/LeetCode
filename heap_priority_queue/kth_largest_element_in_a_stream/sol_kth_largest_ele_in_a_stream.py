import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    class KthLargest:
        def _sift_up(self, i):
            parent = (i - 1) // 2
            while parent >= 0 and self.min_heap[parent] > self.min_heap[i]:
                self.min_heap[parent], self.min_heap[i] = self.min_heap[i], self.min_heap[parent]
                i = parent
                parent = (i - 1) // 2

        def _sift_down(self, i):
            left, right = i * 2 + 1, i * 2 + 2
            while ((left < len(self.min_heap) and self.min_heap[i] > self.min_heap[left]) or
                    (right < len(self.min_heap)) and self.min_heap[i] > self.min_heap[right]):
                smallest = left if (right >= len(self.min_heap) or self.min_heap[left] <= self.min_heap[right]) else right
                self.min_heap[smallest], self.min_heap[i] = self.min_heap[i], self.min_heap[smallest]
                i = smallest
                left, right = i * 2 + 1, i * 2 + 2

        def _heapify(self):
            for i in range(len(self.min_heap))[::-1]:
                self._sift_down(i)

        def _push(self, val):
            self.min_heap.append(val)
            self._sift_up(len(self.min_heap) - 1)

        def _pop(self):
            min_value = self.min_heap[0]
            self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
            self.min_heap.pop()
            self._sift_down(0)
        
        def _simplify(self):
            while len(self.min_heap) > self.kth_largest:
                self._pop()

        def __init__(self, k, nums):
            self.kth_largest = k
            self.min_heap = nums.copy()
            self._heapify()
            self._simplify()

        def add(self, val):
            if len(self.min_heap) < self.kth_largest or self.min_heap[0] < val:
                self._push(val)
                self._simplify()
            return self.min_heap[0]

    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
                                                    
    def test(self, inp, expectation):
        commands, args = inp['commands'], inp['args']
        result_list = []
        for command, argument in zip(commands, args):
            if command == 'KthLargest':
                obj = self.KthLargest(argument[0], argument[1])
                result_list.append(None)
            elif command == 'add':
                val = obj.add(argument[0])
                result_list.append(val)
            else:
                pass

        if result_list == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result_list, color_code['end']))
            
if __name__ == '__main__':
    file_test_case = open('./data_kth_largest_ele_in_a_stream.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)