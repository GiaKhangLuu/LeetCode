import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def checkInclusion(self, s1, s2):
        def add_to_chars_count(chars_count, char):
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1
        
        template_chars_count, subs_chars_count = {}, {}
        start_window, end_window = 0, len(s1)
        for s in s1:
            add_to_chars_count(template_chars_count, s)
        for s in s2[start_window:end_window]:
            add_to_chars_count(subs_chars_count, s)

        while template_chars_count != subs_chars_count:
            start_window += 1
            end_window += 1
            if end_window > len(s2):
                return False
            remove_char = s2[start_window - 1]
            if subs_chars_count[remove_char] == 1:
                subs_chars_count.pop(remove_char)
            else:
                subs_chars_count[remove_char] -= 1 
            add_to_chars_count(subs_chars_count, s2[end_window - 1])

        return True


    def test(self, func, inp, expectation):
        s1, s2 = inp['s1'], inp['s2']
        out = func(s1, s2)

        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_permutation_in_string.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.checkInclusion, inp, expectation)