import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def isAnagram(self, s, t):
        def add_to_dict(my_dict, my_char):
            if my_char in my_dict:
                my_dict[my_char] += 1 
            else:
                my_dict[my_char] = 1

        if len(s) != len(t):
            return False
        s_dict, t_dict = dict(), dict()

        for s_char, t_char in zip(s, t):
            add_to_dict(s_dict, s_char)
            add_to_dict(t_dict, t_char)
        
        if s_dict == t_dict:
            return True
        return False

    def test(self, func, inp, expectation):
        s, t= inp['s'], inp['t']
        out = func(s, t)

        if out == expectation:
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
        solution.test(solution.isAnagram, inp, expectation)


