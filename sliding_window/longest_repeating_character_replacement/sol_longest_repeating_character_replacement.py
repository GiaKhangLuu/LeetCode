import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def characterReplacement(self, s, k):
        longest_len = 1
        l, r = 0, 1
        chars_count = {s[l]: 1}

        while r < len(s):
            r_char = s[r]
            if r_char in chars_count:
                chars_count[r_char] += 1
            else:
                chars_count[r_char] = 1
            max_count_char = max(list(chars_count.values()))
            window_size = r - l + 1
            longest_len = max(longest_len, window_size)
            if window_size - max_count_char > k:
                chars_count[s[l]] -= 1 if chars_count[s[l]] > 0 else 0
                l += 1
                longest_len -= 1
            r += 1

        return longest_len

    def test(self, func, inp, expectation):
        s, k = inp['s'], inp['k']
        out = func(s, k)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_longest_repeating_character_replacement.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.characterReplacement, inp, expectation)