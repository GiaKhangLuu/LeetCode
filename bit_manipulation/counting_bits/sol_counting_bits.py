import json

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    """
    Approach 01: Bit manipulation
    Time complexity: O(n * log(n)) 
    """
    def countBits_bit_manipulation(self, n):
        rs = [0] * len(range(n + 1))
        for i in range(n + 1):
            count = 0
            num = i
            while num != 0:
                count += 1 if num & 1 == 1 else 0
                num >>= 1
            rs[i] = count
        return rs
    
    """
    Approach 02: Dynamic Programming (bottom_up)
    Time complexity: O(n) 
    """
    def countBits_bottom_up(self, n):
        rs = [0] * len(range(n + 1))
        off_set = 1
        for i in range(1, n + 1):
            off_set *= 2 if (i % off_set == 0 and i > 1) else 1
            rs[i] = 1 + rs[i - off_set]
        return rs

    """
    Approach 03: Dynamic Programming (memoization)
    Time complexity: O(n) 
    """
    def countBits_memoization(self, n):
        rs = [0] * len(range(n + 1))
        off_set = 1
        def count(n, off_set):
            if n == 0 or rs[n] != 0:
                return off_set
            off_set = count(n - 1, off_set)
            off_set *= 2 if (n % off_set == 0 and n > 1) else 1
            rs[n] = 1 + rs[n - off_set]
            return off_set

        count(n, 1)
        return rs
 
    def test(self, func, inp, expectation):
        n = inp['n']
        rs = func(n)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_counting_bits.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))

        # Approach 01: Bit manipulation
        #solution.test(solution.countBits_bit_manipulation, inp, expectation)

        # Approach 02: Dynamic Programming (bottom_up)
        #solution.test(solution.countBits_bottom_up, inp, expectation)

        # Approach 03: Dynamic Programming (memoization)
        solution.test(solution.countBits_memoization, inp, expectation)