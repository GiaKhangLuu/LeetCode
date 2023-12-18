import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    class MaxHeap:
        def _sift_up(self, i):
            parent = (i - 1) // 2
            while parent >= 0 and self.my_heap[i] > self.my_heap[parent]:
                self.my_heap[i], self.my_heap[parent] = self.my_heap[parent], self.my_heap[i]
                i = parent
                parent = (i - 1) // 2

        def _sift_down(self, i):
            left, right = i * 2 + 1, i * 2 + 2
            while ((left < len(self.my_heap) and self.my_heap[i] < self.my_heap[left]) or
                    (right < len(self.my_heap) and self.my_heap[i] < self.my_heap[right])):
                largest = left if (right >= len(self.my_heap) or self.my_heap[left] >= self.my_heap[right]) else right
                self.my_heap[i], self.my_heap[largest] = self.my_heap[largest], self.my_heap[i]
                i = largest
                left, right = i * 2 + 1, i * 2 + 2

        def _heapify(self):
            for i in range(len(self.my_heap))[::-1]:
                self._sift_down(i)

        def pop(self):
            if len(self.my_heap):
                self.my_heap[0], self.my_heap[-1] = self.my_heap[-1], self.my_heap[0]
                max_value = self.my_heap.pop()
                self._sift_down(0)
                return max_value
            return None
        
        def push(self, val):
            self.my_heap.append(val)
            self._sift_up(len(self.my_heap) - 1)

        def __init__(self, arr):
            self.my_heap = arr.copy()
            self._heapify()
    
    def lastStoneWeight(self, stones):
        heap = self.MaxHeap(stones)
        while len(heap.my_heap) > 1:
            y, x = heap.pop(), heap.pop()
            if y > x:
                heap.push(y - x)
        return heap.my_heap[0] if len(heap.my_heap) == 1 else 0
                                                    
    def test(self, func, inp, expectation):
        stones = inp['stones']
        rs = func(stones)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))
            
if __name__ == '__main__':
    file_test_case = open('./data_last_stone_weight.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.lastStoneWeight, inp, expectation)