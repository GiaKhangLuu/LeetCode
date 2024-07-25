import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        rs = float('inf')
        min_residue = float('inf')
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            mid_square = mid ** 2
            if mid_square == x:
                return mid
            residue = x - mid_square
            if residue > 0 and residue < min_residue:
                min_residue = residue
                rs = mid
            if mid_square > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return rs

    def test(self, inp, expectation):
        x = inp["x"]

        rs = self.mySqrt(x)

        if rs == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], rs, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i))
        solution.test(inp, expectation)

