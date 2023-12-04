import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    class TimeMap:
        def __init__(self):
            self.hash_map = dict()
        
        def binary_search(self, arr, target):
            l, r = 0, len(arr) - 1
            rs = -1
            while l <= r:
                m = (l + r) // 2
                if target > arr[m]:
                    l = m + 1
                    rs = m
                elif target < arr[m]:
                    r = m - 1
                else:
                    return m
            return rs

        def set(self, key, value, timestamp):
            if key in self.hash_map:
                self.hash_map[key]['values'].append(value)
                self.hash_map[key]['timestamps'].append(timestamp)
            else:
                self.hash_map[key] = {'values': [value], 'timestamps': [timestamp]}

        def get(self, key, timestamp):
            if key in self.hash_map:
                values = self.hash_map[key]['values']
                timestamps = self.hash_map[key]['timestamps']
                if timestamps[0] > timestamp:
                    return ""
                timestamp_prev_idx = self.binary_search(timestamps, timestamp)
                return values[timestamp_prev_idx]
            else:
                return ""
                                                    
    def test(self, inp, expectation):
        commands, args = inp['commands'], inp['args']
        result_list = []

        for command, argument in zip(commands, args):
            if command == 'TimeMap':
                obj = self.TimeMap()
                result_list.append(None)
            elif command == 'set':
                obj.set(key=argument[0], value=argument[1], timestamp=argument[2])
                result_list.append(None)
            else:
                value = obj.get(key=argument[0], timestamp=argument[1])
                result_list.append(value)

        if result_list == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], result_list, color_code['end']))
            
if __name__ == '__main__':
    file_test_case = open('./data_time_based_key_value_store.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)