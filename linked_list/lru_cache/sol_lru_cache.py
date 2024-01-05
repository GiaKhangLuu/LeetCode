import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key, self.value = key, value
        self.next, self.prev = next, prev

class LRUCache:
    def __init__(self, capacity):
        self.max_len = capacity
        self.cache = dict()
        self.head, self.tail = Node(-2, -2), Node(-2, -2)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove_node(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

    def _append_node(self, node):
        most_recent_node, upper_lim_node = self.tail.prev, self.tail
        most_recent_node.next = upper_lim_node.prev = node
        node.prev, node.next = most_recent_node, upper_lim_node

    def get(self, key):
        if key in self.cache.keys():
            node = self.cache[key]
            self._remove_node(node)
            self._append_node(node)
            return self.cache[key].value
        return -1

    def put(self, key, value):
        if key in self.cache.keys():
            node = self.cache[key]
            self._remove_node(node)
            self._append_node(node)
            self.cache[key].value = value
        else:
            new_node = Node(key, value)
            self._append_node(new_node)
            self.cache[key] = new_node

            if len(self.cache.keys()) > self.max_len:
                least_recent_node = self.head.next
                self._remove_node(least_recent_node)
                del self.cache[least_recent_node.key]

class Solution:
                                                    
    def test(self, inp, expectation):
        commands, args = inp['cmds'], inp['args']
        result_list = []
        for command, argument in zip(commands, args):
            if command == 'LRUCache':
                obj = LRUCache(capacity=argument[0])
                result_list.append(None)
            elif command == 'put':
                obj.put(key=argument[0], value=argument[1])
                result_list.append(None)
            else:
                rs = obj.get(key=argument[0])
                result_list.append(rs)

        if result_list == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result_list, color_code['end']))
            
if __name__ == '__main__':
    file_test_case = open('./data_lru_cache.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)
