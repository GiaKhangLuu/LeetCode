import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def topKFrequent(self, nums, k):
        hash_map = dict()

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        freq_and_num = list(zip(hash_map.values(), hash_map.keys()))
        freq_and_num = sorted(freq_and_num, key=lambda x: x[0])
        rs = [num_set[1] for num_set in freq_and_num[len(freq_and_num) - k:]]

        return rs

    def test(self, func, inp, expectation):
        nums, k = inp['nums'], inp['k']
        out = func(nums, k)

        if sorted(out) == sorted(expectation):
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.topKFrequent, inp, expectation)