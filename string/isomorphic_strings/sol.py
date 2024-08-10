import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict, t_dict = dict(), dict()
        for i, (a, b) in enumerate(zip(s, t)):
            if a in s_dict and b in t_dict:
                if s_dict[a] != t_dict[b]:
                    return False
            elif a not in s_dict and b not in t_dict:
                s_dict[a] =  i
                t_dict[b] = i
            else:
                return False
        return True

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
        solution.test(solution.isIsomorphic, inp, expectation)


